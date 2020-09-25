export default {
  // middleware: 'checkauth',
  data() {
    return {
      menu: [
        {
          name: 'Config',
          icon: 'mdi-brain',
          route: '/config'
        },
        {
          name: 'home',
          icon: 'mdi-home',
          route: '/home'
        }
      ]
    }
  },
  computed: {},
  methods: {
    handleLogout() {
      //
      try {
      } catch (error) {
        console.log(error)
      }
      //
      this.$store.dispatch('clearUser')
    }
  }
}
