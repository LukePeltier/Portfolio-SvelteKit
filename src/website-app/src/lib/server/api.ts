import PocketBase from 'pocketbase';
import { API_USER, API_PASS } from '$env/static/private';

export class Api {
  client: PocketBase;

  constructor() {
    this.client = new PocketBase('http://host.docker.internal:8090');
  }

  async authenticate() {
    await this.client.admins.authViaEmail(API_USER, API_PASS);
  }

  async getPlayers() {
    const resultList = await this.client.records.getList('player', 1, Number.MAX_SAFE_INTEGER);
    return resultList;
  }

  async getGameLanesByPlayer(player: string) {
    const resultList = await this.client.records.getList('gameLaner', 1, Number.MAX_SAFE_INTEGER, {
      filter: `player.id = "${player}"`,
      expand: `game`
    });
    return resultList;
  }
}
