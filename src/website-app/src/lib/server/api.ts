import PocketBase from 'pocketbase';
import { API_USER, API_PASS, API_URL } from '$env/static/private';

export class Api {
  client: PocketBase;

  constructor() {
    this.client = new PocketBase(API_URL);
  }

  async authenticate() {
    try {
      await this.client.admins.authWithPassword(API_USER, API_PASS);
    } catch (err) {
      console.log(err);
      return false;
    }
    return true;
  }

  async getPlayers() {
    const resultList = await this.client.collection('player').getFullList();
    return resultList;
  }

  async getGameLanesByPlayer(player: string) {
    const resultList = await this.client.collection('gameLaner').getFullList({
      filter: `player.id = "${player}"`,
      expand: `game`
    });
    return resultList;
  }
}
