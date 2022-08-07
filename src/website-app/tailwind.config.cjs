/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  theme: {
    extend: {
      fontFamily: {
        'lato': ['Lato'],
        'robotomono': ['Roboto Mono']
      }
    },
  },
  plugins: []
};