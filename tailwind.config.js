module.exports = {
  content: [
    './templates/**/*.html',
    './kovsie_connections/templates/**/*.html',
    './static/**/*.js',
    './node_modules/flowbite/**/*.js'
  ],
  theme: {
    extend: {
      colors: {
        navy: {
          800: '#003366',  // Navy color for the background
        },
        red: {
          600: '#c8102e',  // Red color for the spinner
        },
      },
    },
  },
  plugins: [
    require('flowbite/plugin'),
  ],
}
