/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      fontFamily: {
        lato: ['Lato'],
        robotomono: ['Roboto Mono'],
        tenmans: ['Gill Sans', 'Lato', 'ui-sans-serif'],
        tenmansbold: ['Gill Sans Bold']
      },
      colors: {
        statisticRed: '#c05d84',
        statisticBlue: '#45a1ca',
        oldTenMansYellow: '#ffc107'
      }
    }
  },
  plugins: [require('daisyui')],
  daisyui: {}
};
