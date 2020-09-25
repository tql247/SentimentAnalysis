<template>
  <v-app>
    <v-navigation-drawer mini-variant app light color="#BDBDBD">
      <div class="fill-height d-flex flex-column">
        <v-list class="flex-grow-1"> </v-list>
        <v-list>
          <v-tooltip right nudge-right="10">
            <template v-slot:activator="{ on }">
              <v-list-item @click="handleLogout" v-on="on">
                <v-list-item-action>
                  <v-icon>mdi-power</v-icon>
                </v-list-item-action>
                <v-list-item-content>
                  <v-list-item-title v-text="'Log out ' + 'user.name'" />
                </v-list-item-content>
              </v-list-item>
            </template>
            <span>Thoát "{{ user }}"?</span>
          </v-tooltip>
        </v-list>
      </div>
    </v-navigation-drawer>
    <v-content class="">
      <nuxt />
    </v-content>
  </v-app>
</template>

<script src="./index.js"></script>
<style scoped></style>
