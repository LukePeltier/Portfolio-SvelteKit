const { neutral } = require('daisyui/src/colors');

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
  daisyui: {
    themes: [
      'dark',
      'black',
      'night',
      {
        ugg: {
          primary: '#f3f4f6',
          secondary: '#191937',
          accent: '#3273fa',
          neutral: '#070720',
          'base-100': '#0d0d28',
          info: '#6198D6',
          success: '#4AE39C',
          warning: '#eda7aa',
          error: '#ff4e50',
          'text-neutral-content': '#ffffff'
        }
      }
    ]
  }
};
