export default {
  layout: 'app',
  data() {
    return {
      isLoading: false,
      playground: [
        {
          header: 'Embedding',
          option: [
            {
              title: '...',
              isPick: false,
              des: 'Word'
            },
            {
              title: '...',
              isPick: true,
              des: 'Character'
            }
          ]
        },
        {
          header: 'Model',
          option: [
            {
              title: 'CNN',
              isPick: true,
              des: 'CNN'
            },
            {
              title: 'RNN',
              isPick: false,
              des: 'RNN'
            },
            {
              title: 'LSTM',
              isPick: false,
              des: ''
            }
          ]
        },
        {
          header: 'Active funtion',
          option: [
            {
              title: 'Linear',
              isPick: false,
              des: ''
            }
          ]
        },
        {
          header: 'Loss',
          option: [
            {
              title: 'Cross Entropy',
              isPick: true,
              des: ''
            }
          ]
        }
      ],
      showDescription: 'linear',
      Embedding: 'character',
      Model: 'lstm',
      activeFunc: 'linear',
      lossFunc: 'crossEntropy'
    }
  },
  computed: {},
  methods: {
    changeOption(header, ls, newPick) {
      for (let i = 0; i < ls.length; i++) {
        ls[i].isPick = false
      }
      newPick.isPick = true

      switch (header) {
        case 'Embedding':
          this.Embedding = newPick
          break

        case 'Model':
          this.Model = newPick
          break
      }
    },
    async requestOption() {
      const param = {
        embedding: this.Embedding,
        model: this.Model,
        active: this.activeFunc,
        loss: this.lossFunc
      }

      const axios = require('axios')
      const data = JSON.stringify(param)

      const config = {
        method: 'post',
        url: 'http://localhost/setter',
        headers: {
          'Content-Type': 'application/json'
        },
        data
      }

      await axios(config)
        .then(function(response) {
          console.log(JSON.stringify(response.data))
        })
        .catch(function(error) {
          console.log(error)
        })
    },
    previewFeature(option) {
      this.showDescription = option.des
    }
  }
}
