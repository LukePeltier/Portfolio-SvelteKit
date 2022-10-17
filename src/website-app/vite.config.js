import { sveltekit } from '@sveltejs/kit/vite';
// eslint-disable-next-line @typescript-eslint/no-var-requires
import * as path from 'path';

/** @type {import('vite').UserConfig} */
const config = {
  plugins: [sveltekit()],
  resolve: {
    alias: {
      $static: path.resolve(__dirname, './static')
    }
  }
};

export default config;
