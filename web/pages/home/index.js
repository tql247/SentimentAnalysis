export default {
  layout: 'app',
  data() {
    return {
      text: '',
      predict: 'Positive',
      prob: '...',
      isLoading: false,
      predictImg: '/smile.png'
    }
  },
  computed: {},
  methods: {
    async getPredict() {
      this.isLoading = true
      const axios = require('axios')

      const config = {
        method: 'get',
        url: 'http://localhost:80/sean/' + this.text,
        headers: {
          'Access-Control-Allow-Origin': '*',
          'Access-Control-Allow-Methods': 'GET,PUT,POST,DELETE',
          'Access-Control-Allow-Headers': 'Content-Type'
        }
      }

      try {
        const response = await axios(config)
        const resVal = response.data.label
        console.log(resVal)

        switch (resVal) {
          case 'Negative':
            this.predict = 'Negative'
            this.predictImg = '/neg.png'
            break

          case 'Normal':
            this.predict = 'Normal'
            this.predictImg = '/nor.png'
            break

          case 'Positive':
            this.predict = 'Positive'
            this.predictImg = '/smile.png'
            break
        }
      } catch (e) {
        this.$toast.error(e)
      }

      this.isLoading = false
    }
  }
}
