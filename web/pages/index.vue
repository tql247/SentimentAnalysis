<template>
  <div></div>
</template>

<script>
export default {
  data() {
    return {}
  },
  mounted() {
    this.$nextTick(() => {
      // return this.$router.push('/login')
      return this.$router.push('/home')
    })
  },
  methods: {}
}
</script>
