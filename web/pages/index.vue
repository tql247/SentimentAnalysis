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
      return this.$router.push('/login')
    })
  },
  methods: {}
}
</script>
