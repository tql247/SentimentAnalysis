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
              des: 'a'
            },
            {
              title: '...',
              isPick: true,
              des: 'asdas'
            }
          ]
        },
        {
          header: 'Model',
          option: [
            {
              title: 'MGAN',
              isPick: true,
              des: '1231dzda'
            },
            {
              title: 'LSTM',
              isPick: false,
              des: '12dA34'
            },
            {
              title: 'TNet',
              isPick: false,
              des: '12FAFAWE  E34'
            }
          ]
        },
        {
          header: 'Active funtion',
          option: [
            {
              title: 'Cos Sin',
              isPick: false,
              des: '12AVCSC AAS34'
            },
            {
              title: 'Sigmod',
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
