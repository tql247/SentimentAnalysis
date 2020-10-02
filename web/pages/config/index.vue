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

    <v-row class="app-content d-flex">
      <v-col cols="12" sm="12" md="10" lg="6" xl="6">
        <v-alert class="intro mx-2" dense outlined type="info">
          Với mỗi trường hợp khác nhau nên lựa chọn các phương pháp embedding,
          model, loss và active function sao cho phù hợp.
        </v-alert>
        <div class="model-playground">
          <div v-for="(item, key) in playground" :key="key" class="prow">
            <div class="header">
              <div class="item">
                {{ item.header }}
              </div>
            </div>
            <div class="option">
              <div
                v-for="(option, key) in item.option"
                :key="key"
                :class="'item ' + (option.isPick === true ? 'active' : '')"
                @click="changeOption(item.option, option)"
                @mouseover="previewFeature(option)"
              >
                <div class="item-content">
                  {{ option.title }}
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="px-1 mt-3 fill-width">
          <v-btn tile class="fill-width active-btn" depressed color="success">
            Use
          </v-btn>
        </div>
      </v-col>
      <v-col class="description" cols="12" sm="12" md="10" lg="6" xl="6">
        <v-card flat class="content">
          {{ showDescription }}
        </v-card>
      </v-col>
    </v-row>
  </div>
</template>

<script src="./index.js"></script>
<style lang="scss" src="./index.scss" scoped></style>
