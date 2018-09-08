module.exports = {
  /*
  ** Headers of the page
  */
  head: {
    title: 'devhackfest',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      { hid: 'description', name: 'description', content: 'Devcon Academia' }
    ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' }
    ],
    script: [
      { src: 'js/jquery.js' },
      { src: 'js/bootstrap.min.js' },
      { src: 'js/jquery.counterup.min.js' },
      { src: 'js/jquery.jCounter.js' },
      { src: 'js/waypoints.min.js' },
      { src: 'js/jquery.colorbox.js' },
      { src: 'js/smoothscroll.js' },
      { src: 'js/custom.js' }
    ]
  },
  css: [
    'assets/css/bootstrap.min.css',
    'assets/css/style.css',
    'assets/css/responsive.css',
    'assets/css/font-awesome.min.css',
    'assets/css/animate.css'
  ],
  /*
  ** Customize the progress bar color
  */
  loading: { color: '#3B8070' },
  /*
  ** Build configuration
  */
  build: {
    /*
    ** Run ESLint on save
    */
    extend (config, ctx) {
      if (ctx.dev && ctx.isClient) {
        config.module.rules.push({
          enforce: 'pre',
          test: /\.(js|vue)$/,
          loader: 'eslint-loader',
          exclude: /(node_modules)/
        })
      }
    }
  }
}
