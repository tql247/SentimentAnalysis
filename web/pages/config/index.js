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
      showDescription: 'abc'
    }
  },
  computed: {},
  methods: {
    changeOption(ls, newPick) {
      console.log(ls)
      for (let i = 0; i < ls.length; i++) {
        ls[i].isPick = false
      }

      newPick.isPick = true
    },
    previewFeature(option) {
      this.showDescription = option.des
    }
  }
}
