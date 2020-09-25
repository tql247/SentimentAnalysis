export default {
  middleware: 'checkauth',
  data() {
    return {}
  },
  computed: {
    user() {
      return this.$auth.user.identity
    }
  },
  methods: {
    handleLogout() {
      //
      try {
        this.$auth.logout()
      } catch (error) {
        console.log(error)
      }
      //
      this.$store.dispatch('clearUser')
      return this.$router.push('/login')
    }
  }
}
