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
        statisticRed: '#ff4e50',
        statisticBlue: '#3273fa',
        oldTenMansYellow: '#ffc107'
      }
    }
  },
  plugins: [require('daisyui')],
  daisyui: { themes: ['dark', 'black'] }
};
