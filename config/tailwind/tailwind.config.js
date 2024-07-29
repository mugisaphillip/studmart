/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "../../src/templates/**/*.html"
  ],
  theme: {
    extend: {
      gridTemplateColumns: {
        'hero': '0.7fr 1fr',
      }},
  },
  plugins: [
    require('@tailwindcss/typography'),
  ],
}

