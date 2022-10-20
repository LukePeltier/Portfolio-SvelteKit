import { Api } from '$lib/server/api';
import type { PageServerLoad } from './$types';

// eslint-disable-next-line @typescript-eslint/no-unused-vars
export const load: PageServerLoad = async ({ params }) => {
  const api = new Api();
  await api.authenticate();

  const players = await api.getPlayers();

  const rows: {
    name: string;
    top: number;
    jungle: number;
    mid: number;
    bot: number;
    support: number;
  }[] = [];

  for (const player of players.items) {
    const name = player['name'];

    const gameLaners = await api.getGameLanesByPlayer(player['id']);
    const games: { [index: string]: number } = { Top: 0, Jungle: 0, Mid: 0, Bot: 0, Support: 0 };
    for (const gameLaner of gameLaners.items) {
      const lane: string = gameLaner['lane'];
      games[lane] += 1;
    }

    rows.push({
      name: name,
      top: games.Top,
      jungle: games.Jungle,
      mid: games.Mid,
      bot: games.Bot,
      support: games.Support
    });
  }

  return {
    rows: rows
  };
};
