<template>
  <v-container class="fill-height">
    <v-overlay :value="isLoading">
      <div class="process-bar" align="center">
        <v-progress-circular
          :size="50"
          color="amber"
          indeterminate
        ></v-progress-circular>
      </div>
    </v-overlay>

    <v-row class="login-form fill-height">
      <v-col cols="12" sm="7" md="6" lg="5" xl="4">
        <v-card class="elevation-12 form-padding">
          <div class="form-header">
            <div class="form-title" align="center">
              Đăng nhập
            </div>
          </div>
          <v-card-text class="form-text">
            <v-form>
              <v-text-field
                id="username"
                v-model="username"
                label="Tài khoản"
                name="login"
                prepend-icon="mdi-account"
                type="text"
                class="form-value"
              ></v-text-field>

              <v-text-field
                id="password"
                v-model="password"
                label="Mật khẩu"
                name="password"
                prepend-icon="mdi-lock"
                class="form-value"
                type="password"
              ></v-text-field>
            </v-form>
          </v-card-text>
          <v-card-actions>
            <v-spacer></v-spacer>
            <v-btn
              rounded
              color="#1E88E5"
              class="full-width submit submit-btn"
              @click="submit()"
            >
              Kiểm tra
            </v-btn>
          </v-card-actions>
          <div class="form-message"></div>
          <br />
        </v-card>
      </v-col>
    </v-row>
  </v-container>
</template>

<script src="./index.js"></script>
<style lang="scss" src="./index.scss" scoped></style>
