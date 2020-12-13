const colors = require('tailwindcss/colors');
module.exports = {
  purge: [
      '**/**/templates/**/*.html'
  ],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        gray: colors.trueGray,
        red: colors.red,
        blue: colors.lightBlue,
        yellow: colors.yellow,
        teal: colors.teal,
        fuchsia: colors.fuchsia,
        coolGray: colors.coolGray,
        orange: colors.orange,
        amber: colors.amber,
        lime: colors.lime,
        cyan: colors.cyan,
        rose: colors.rose
      }
    },
  },
  variants: {
    extend: {},
  },
  plugins: [],
}
