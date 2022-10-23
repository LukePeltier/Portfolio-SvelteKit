import { Api } from '$lib/server/api';
import type { PageServerLoad } from './$types';

// eslint-disable-next-line @typescript-eslint/no-unused-vars
export const load: PageServerLoad = async ({ params }) => {
  const api = new Api();
  await api.authenticate();

  const players = await api.getPlayers();

  const gamesPlayedRows: {
    name: string;
    top: number;
    jungle: number;
    mid: number;
    bot: number;
    support: number;
  }[] = [];

  const gamesWonRows: {
    name: string;
    top: string;
    jungle: string;
    mid: string;
    bot: string;
    support: string;
  }[] = [];

  for (const player of players.items) {
    const name = player['name'];

    const gameLaners = await api.getGameLanesByPlayer(player['id']);
    const games: { [index: string]: number } = { Top: 0, Jungle: 0, Mid: 0, Bot: 0, Support: 0 };
    const gamesWon: { [index: string]: number } = { Top: 0, Jungle: 0, Mid: 0, Bot: 0, Support: 0 };
    for (const gameLaner of gameLaners.items) {
      const lane: string = gameLaner['lane'];
      games[lane] += 1;
      if (gameLaner['@expand']['game']['winner'] == gameLaner['team']) {
        gamesWon[lane] += 1;
      }
    }

    gamesPlayedRows.push({
      name: name,
      top: games.Top,
      jungle: games.Jungle,
      mid: games.Mid,
      bot: games.Bot,
      support: games.Support
    });

    gamesWonRows.push({
      name: name,
      top: winsToPercentString(games.Top, gamesWon.Top),
      jungle: winsToPercentString(games.Jungle, gamesWon.Jungle),
      mid: winsToPercentString(games.Mid, gamesWon.Mid),
      bot: winsToPercentString(games.Bot, gamesWon.Bot),
      support: winsToPercentString(games.Support, gamesWon.Support)
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