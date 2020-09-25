export const state = () => ({
  authenticate: {
    user: '',
    token: ''
  }
})

export const mutations = {
  setAuthenticate(state, { auth }) {
    state.authenticate = auth
  },
  clearAuthenticate(state) {
    state.authenticate = { user: '', token: '' }
  }
}

export const actions = {
  setUser({ commit }, { auth }) {
    commit('setAuthenticate', { auth })
  },
  clearUser({ commit }) {
    commit('clearAuthenticate')
  }
}
