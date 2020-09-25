export default {
  // middleware: 'checkauth',
  data() {
    return {
      menu: [
        {
          name: 'Document',
          icon: 'mdi-file-document-outline',
          route: '/document'
        },
        {
          name: 'Config',
          icon: 'mdi-brain',
          route: '/config'
        },
        {
          name: 'Statistics',
          icon: 'mdi-chart-bar',
          route: '/statistics'
        },
        {
          name: 'Home',
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
