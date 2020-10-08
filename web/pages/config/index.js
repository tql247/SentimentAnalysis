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
              title: '...',
              isPick: true,
              des: '1231dzda'
            },
            {
              title: '...',
              isPick: false,
              des: '12dA34'
            },
            {
              title: '... .................',
              isPick: false,
              des: '12FAFAWE  E34'
            }
          ]
        },
        {
          header: 'Active funtion',
          option: [
            {
              title: '...',
              isPick: false,
              des: '12AVCSC AAS34'
            },
            {
              title: '...',
              isPick: false,
              des: '1 ASDASD ASD234'
            },
            {
              title: '...',
              isPick: true,
              des: '1 ASDASD ASD234'
            }
          ]
        },
        {
          header: 'Loss',
          option: [
            {
              title: '...',
              isPick: true,
              des: '1FASFwfQW234'
            },
            {
              title: '...',
              isPick: false,
              des: 'ffasfasd'
            },
            {
              title: '...',
              isPick: false,
              des: 'ASDasdASDASDQE'
            },
            {
              title: '...',
              isPick: false,
              des: 'w'
            }
          ]
        }
      ],
      showDescription: 'abc',
      Embedding: 'a',
      Model: 'v',
      activeFunc: 'as',
      lossFunc: '1'
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
