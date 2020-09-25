<template>
  <div class="page-content grey lighten-5">
    <v-overlay :value="isLoading">
      <div class="process-bar">
        <v-progress-circular
          :size="50"
          color="amber"
          indeterminate
        ></v-progress-circular>
      </div>
    </v-overlay>

    <div class="app-content d-flex"></div>
  </div>
</template>

<script src="./index.js"></script>
<style lang="scss" src="./index.scss" scoped></style>
