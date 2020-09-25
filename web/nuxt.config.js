require('dotenv').config()

export default {
  mode: 'spa',
  /*
   ** Headers of the page
   */
  head: {
    titleTemplate: '%s - Tải văn bản',
    title: 'FUI' || '',
    meta: [
      { charset: 'utf-8' },
      { name: 'viewport', content: 'width=device-width, initial-scale=1' },
      {
        hid: 'description',
        name: 'description',
        content: process.env.npm_package_description || ''
      }
    ],
    // script: [
    //   {src: 'https://webgl2fundamentals.org/webgl/resources/webgl-utils.js'}
    // ],
    link: [
      { rel: 'icon', type: 'image/x-icon', href: '/favicon.ico' },
      {
        rel: "stylesheet",
        href: "https://fonts.googleapis.com/css2?family=Roboto+Slab:wght@500&display=swap",
      },
      {
        rel: "stylesheet",
        href: "https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@300&display=swap",
      },
      {
        rel: "stylesheet",
        href: "https://fonts.googleapis.com/css2?family=Comfortaa:wght@700&display=swap",
      },
      {
        rel: "stylesheet",
        href: "https://fonts.googleapis.com/css2?family=Raleway:wght@500&display=swap",
      },
      {
        rel: "stylesheet",
        href: "https://fonts.googleapis.com/css2?family=MuseoModerno:wght@400;500&display=swap",
      },
      {
        rel: "stylesheet",
        href: "https://fonts.googleapis.com/css2?family=Kufam&display=swap",
      },
      {
        rel: "stylesheet",
        href: "https://fonts.googleapis.com/css2?family=Josefin+Sans&display=swap",
      },
    ]
  },
  /*
   ** Customize the progress-bar color
   */
  loading: {
    color: '#0078D7',
    throttle: 0,
    continuous: true
  },
  /*
   ** Global CSS
   */
  css: [
    '@/assets/main.scss',
    '@/assets/animate.min.css',
    '@/node_modules/sweetalert2/dist/sweetalert2.min.css'
  ],
  /*
   ** Plugins to load before mounting the App
   */
  plugins: [
    "~/plugins/veevalidate.js",
    '~/plugins/globalComponents.js',
  ],
  /*
   ** Nuxt.js dev-modules
   */
  buildModules: [
    '@nuxtjs/eslint-module',
    '@nuxtjs/vuetify',
    '@nuxtjs/dotenv'
  ],
  eslint: {
    fix: true
  },
  /*
   ** Nuxt.js modules
   */
  modules: [
    '@nuxtjs/axios',
    '@nuxtjs/pwa',
    '@nuxtjs/dotenv',
    '@nuxtjs/axios',
    '@nuxtjs/auth',
    '@nuxtjs/toast',
    ['vue-sweetalert2/nuxt',{
      icon: 'warning',
      title: 'Vui lòng xác nhận',
      confirmButtonColor: '#F57C00',
      confirmButtonText: 'Đồng ý',
      cancelButtonText: 'Hủy bỏ',
      showCancelButton: true,
      reverseButtons: true,
    }],
  ],
  // env: {
  //   wsUrl: process.env.WS_URL || 'ws://192.168.2.102:4000',
  //   pulsarConsume: process.env.PULSAR_CONSUME || ''
  // },
  toast: {
      position: 'bottom-right',
      duration: 2000
  },
  /*
   ** Axios module configuration
   ** See https://axios.nuxtjs.org/options
   */
  axios: {
    baseURL: 'http://115.79.43.243:7600/service',
    browserBaseURL: 'http://115.79.43.243:7600/service'
  },
  auth: {
    strategies: {
      local: {
        endpoints: {
          login: { url: '/toollogin', method: 'post', propertyName: false },
          user: { url: '/toollogin/me', method: 'get', propertyName: 'user' },
          logout: { url: '/toollogin/logout', method: 'post'},
        },
        tokenRequired: true,
        tokenType: 'bearer',
        autoFetchUser: false
      }
    },
    redirect: false
  },
  /*
   ** vuetify module configuration
   ** https://github.com/nuxt-community/vuetify-module
   */
  vuetify: {
    customVariables: ['~/assets/variables.scss'],
    optionsPath: './vuetify.options.js'
  },
  /*
   ** Build configuration
   */
  build: {
    transpile: ["vee-validate/dist/rules"],
    /*
     ** You can extend webpack config here
     */
    extend(config, ctx) {
      config.node = {
        fs: "empty"
      }
    }
  },
  layoutTransition: {
    name: 'layout',
    mode: 'out-in'
  },
  pageTransition: {
    name: 'page',
    mode: 'out-in'
  },
  // server: {
  //   host: '0.0.0.0' // default: localhost
  // }
}
