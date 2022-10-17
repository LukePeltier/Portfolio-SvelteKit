import { sveltekit } from '@sveltejs/kit/vite';
// eslint-disable-next-line @typescript-eslint/no-var-requires
import * as path from 'path';

/** @type {import('vite').UserConfig} */
const config = {
  plugins: [sveltekit()]
};

export default config;
