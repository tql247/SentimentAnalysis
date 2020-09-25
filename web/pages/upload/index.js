export default {
  layout: 'app',
  data() {
    return {
      open: true,
      isLoading: false,
      items: [],
      items3: [],
      fileData: {
        fileName: 'base64'
      },
      previewData: '',
      checkDublicate: []
    }
  },
  computed: {
    user() {
      return this.$auth.user.identity
    }
  },
  methods: {
    chooseFileUpload(event, args) {
      if (args === 'main') this.$refs.mainfilesUpload.click()
      else event.target.parentNode.querySelector('input').click()
    },
    updateListHeight(crrAttachListId, iconId) {
      if (document.querySelector('#' + crrAttachListId)) {
        const self = this
        setTimeout(function() {
          document.querySelector('#attachitemid0').style.height =
            document.querySelector('#attachitemid0').scrollHeight + 'px'

          self.activeAttach(crrAttachListId, iconId)
        }, 100)
      }
    },
    readMultiFileAsDataURL(event, args, mainFileName, crrAttachListId, iconId) {
      const reader = new FileReader()
      const files = event.target.files
      const self = this

      function readFile(index) {
        if (index >= files.length) {
          event.target.value = ''
          self.updateListHeight(crrAttachListId, iconId)
          return
        }
        const file = files[index]

        reader.onload = function() {
          const fileName = file.name
          if (!self.checkDublicate.includes(fileName)) {
            if (args === 'main') {
              self.items.push({ fileName, lsAttach: [] })
            } else {
              // get index of object with id:37
              const index = self.items
                .map(function(item) {
                  return item.fileName
                })
                .indexOf(mainFileName)

              self.items[index].lsAttach.push(file.name)
            }

            const dataURL = reader.result
            self.fileData[file.name] = dataURL
            self.checkDublicate.push(file.name)
          }
          readFile(index + 1)
        }
        reader.readAsDataURL(file)
      }

      readFile(0)
    },
    handlePreview(fileName) {
      this.previewData = fileName
    },
    cancelQueue() {
      for (let i = 0; i < this.items.length; i++) {
        delete this.fileData[this.items[i].fileName]
        for (let j = 0; j < this.items[i].lsAttach.length; j++) {
          delete this.fileData[this.items[i].lsAttach[j]]
        }
      }
      this.items = []
      this.checkDublicate = []
    },
    clearQueue() {
      this.items = []
      this.checkDublicate = []
    },
    combineParam(fileName) {
      const listAttach = []

      const index = this.items
        .map(function(items) {
          return items.fileName
        })
        .indexOf(fileName)

      // get list attach
      for (let i = 0; i < this.items[index].length; i++) {
        const base64Attach = this.fileData[this.items[index][i].fileName]

        listAttach.push({
          content: base64Attach.replace(/data.*base64,/g, ''),
          tenFile: this.items[index][i]
        })
      }

      const param = {
        user: this.user,
        loaixuly: 1,
        doc: {
          content: this.fileData[fileName].replace(/data.*base64,/g, ''),
          tenFile: fileName
        },
        attach: listAttach
      }

      return param
    },
    async uploadFile() {
      if (this.items.length === 0) return
      this.isLoading = true

      const self = this

      async function uploadRecursive(index) {
        if (index >= self.items.length) {
          self.$toast.success('Tải xong')
          self.clearQueue()
          self.isLoading = false
          return
        }

        const fileName = self.items[index].fileName
        const url = '/upload/base64/tool'
        const param = self.combineParam(fileName)
        const headers = {
          'Content-Type': 'application/json'
        }

        try {
          const response = await self.$axios.$post(url, param, headers)

          if (response.status !== 0) throw response.status

          self.markFileIsUploaded(fileName)
        } catch (error) {
          if (error === '401') {
            self.$toast.error('Phiên đăng nhập hết hạn')
            return self.$router.push('/login')
          }
          self.$toast.error('Lỗi tải ' + fileName)
        }

        uploadRecursive(index + 1)
      }

      await uploadRecursive(0)
    },
    markFileIsUploaded(fileName) {
      const index = this.items
        .map(function(items) {
          return items.fileName
        })
        .indexOf(fileName)
      this.items3.push({
        id: this.items3.length,
        fileName,
        attach: this.items[index].lsAttach
      })
    },
    removeFile(fileName) {
      // get index of object with id:37
      const removeIndex = this.items
        .map(function(item) {
          return item.fileName
        })
        .indexOf(fileName)

      // remove object
      this.items.splice(removeIndex, 1)
      this.checkDublicate.splice(this.checkDublicate.indexOf(fileName), 1)
      delete this.fileData[fileName]
    },
    removeAttach(event, mainFileName, attachFileName) {
      const target = event.target.closest('.list-attach.drawer')

      target.style.height =
        target.firstChild.scrollHeight *
          (target.querySelectorAll('.item-attach').length - 1) +
        'px'

      if (target.querySelectorAll('.item-attach').length - 1 <= 0) {
        target.style.height = '100%'
      }

      const index = this.items
        .map(function(item) {
          return item.fileName
        })
        .indexOf(mainFileName)

      this.checkDublicate.splice(this.checkDublicate.indexOf(attachFileName), 1)

      this.items[index].lsAttach.splice(
        this.items[index].lsAttach.indexOf(attachFileName),
        1
      )
      delete this.fileData[attachFileName]
    },
    activeAttach(crrAttach, iconId) {
      const target = document.querySelector('#' + iconId)
      if (target.className.includes('active')) {
        this.collapseAttach(iconId, crrAttach)
      }
    },
    collapseAttach(iconId, crrAttach) {
      const target = document.querySelector('#' + iconId)
      try {
        if (target.className.includes('active')) {
          target.classList.remove('active')
          if (document.querySelector('#' + crrAttach).scrollHeight > 0) {
            document.querySelector('#' + crrAttach).style.height =
              document.querySelector('#' + crrAttach).scrollHeight + 'px'
            document.querySelector('#' + crrAttach).classList.remove('active')
          }
        } else {
          target.classList.add('active')
          if (document.querySelector('#' + crrAttach).scrollHeight > 0) {
            document.querySelector('#' + crrAttach).style.height =
              document.querySelector('#' + crrAttach).scrollHeight + 'px'
            document.querySelector('#' + crrAttach).classList.add('active')
          }
        }
      } catch (error) {
        console.log(error)
      }
    }
  }
}
