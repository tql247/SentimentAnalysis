export default {
  data() {
    return {
      isLoading: false,
      username: '',
      password: ''
    }
  },
  methods: {
    async submit() {
      if (this.username === '' || this.password === '') {
        this.$toast.error('Bạn chưa nhập đủ thông tin')
      }

      this.isLoading = true

      try {
        await this.$auth.loginWith('local', {
          data: {
            username: this.username,
            password: this.password
          }
        })
        await this.$auth.setUser({
          identity: this.username
        })
        this.$router.push('/upload')
      } catch (error) {
        this.$toast.error(error.response.data.message)
      }
      this.isLoading = false
    }
  }
}
