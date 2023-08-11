import { Api } from '$lib/server/api';
import { error } from '@sveltejs/kit';
import { Record } from 'pocketbase';
import type { PageServerLoad } from './$types';

export type PlayerGamesPlayed = {
  name: string;
  top: number;
  jungle: number;
  mid: number;
  bot: number;
  support: number;
  total: number;
};

export type PlayerGamesWon = {
  name: string;
  top: string;
  jungle: string;
  mid: string;
  bot: string;
  support: string;
  total: string;
};

// eslint-disable-next-line @typescript-eslint/no-unused-vars
export const load: PageServerLoad = async ({ params }) => {
  const api = new Api();
  const authResult = await api.authenticate();
  if (!authResult) {
    throw error(500, 'Unable to authenticate with API');
  }

  const players = await api.getPlayers();

  const gamesPlayedRows: PlayerGamesPlayed[] = [];

  const gamesWonRows: PlayerGamesWon[] = [];

  for (const player of players) {
    const name = player['name'];

    const gameLaners = await api.getGameLanesByPlayer(player['id']);
    const games: { [index: string]: number } = { Top: 0, Jungle: 0, Mid: 0, Bot: 0, Support: 0 };
    const gamesWon: { [index: string]: number } = { Top: 0, Jungle: 0, Mid: 0, Bot: 0, Support: 0 };
    let totalGamesWon = 0;
    let totalGames = 0;
    for (const gameLaner of gameLaners) {
      const game = gameLaner.expand['game'];
      if (!(game instanceof Record)) {
        throw error(500, 'Unexpectedly expanded to list of records instead of single record');
      }
      const lane: string = gameLaner['lane'];
      games[lane] += 1;
      totalGames += 1;
      if (game['winner'] == gameLaner['team']) {
        gamesWon[lane] += 1;
        totalGamesWon += 1;
      }
    }

    gamesPlayedRows.push({
      name: name,
      top: games.Top,
      jungle: games.Jungle,
      mid: games.Mid,
      bot: games.Bot,
      support: games.Support,
      total: totalGames
    });

    gamesWonRows.push({
      name: name,
      top: winsToPercentString(games.Top, gamesWon.Top),
      jungle: winsToPercentString(games.Jungle, gamesWon.Jungle),
      mid: winsToPercentString(games.Mid, gamesWon.Mid),
      bot: winsToPercentString(games.Bot, gamesWon.Bot),
      support: winsToPercentString(games.Support, gamesWon.Support),
      total: winsToPercentString(totalGames, totalGamesWon)
    });
  }

  return {
    gamesPlayed: gamesPlayedRows,
    gamesWon: gamesWonRows
  };
};

function winsToPercentString(laneNum: number, laneWins: number) {
  const lanePercent: number = (laneWins / laneNum) * 100;
  let lanePercentString: string;
  if (isNaN(lanePercent)) {
    lanePercentString = 'N/A';
  } else {
    lanePercentString = lanePercent.toFixed(2).toString() + '%';
  }

  return lanePercentString;
}
