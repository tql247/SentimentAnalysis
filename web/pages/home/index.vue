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

    <v-container class="my-style">
      <v-row>
        <v-col cols="12" sm="12" md="12" lg="8" xl="10">
          <div class="v-align-center">
            <v-text-field
              light
              prepend-inner-icon="mdi-comment"
              label="Input"
              rows="1"
            ></v-text-field>
            <v-btn class="ml-4" @click="1">Check</v-btn>
          </div>
        </v-col>
      </v-row>

      <v-row>
        <v-rol cols="12" sm="12" md="12" lg="8" xl="10">
          <div>
            <v-card light class="mx-3" outlined>
              <v-list-item three-line>
                <v-list-item-content>
                  <div class="overline mb-4">Result</div>
                  <v-list-item-title class="headline mb-1">
                    {{ predict }}
                  </v-list-item-title>
                  <v-list-item-subtitle>
                    {{ prob }}
                  </v-list-item-subtitle>
                </v-list-item-content>

                <v-list-item-avatar tile size="80">
                  <v-img src="/smile.png"> </v-img>
                </v-list-item-avatar>
              </v-list-item>

              <v-card-actions>
                <v-btn text color="success">
                  <span class="v-align-end">
                    Correct
                    <v-icon>
                      mdi-check
                    </v-icon>
                  </span>
                </v-btn>
                <v-btn text color="error">
                  <span class="v-align-end">
                    Wrong
                    <v-icon>
                      mdi-bug
                    </v-icon>
                  </span>
                </v-btn>
              </v-card-actions>
            </v-card>
          </div>
          <br />
        </v-rol>
      </v-row>
    </v-container>
  </div>
</template>

<script src="./index.js"></script>
<style lang="scss" src="./index.scss" scoped></style>
