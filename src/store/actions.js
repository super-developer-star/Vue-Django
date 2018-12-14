export default {
  setProgressStatus: ({ commit }, status) => {
    commit('isProgressStatus', status)
  },
  login: ({ commit }, auth) => {
    commit('isLoggedIn', auth)
  },
  setUser: ({ commit }, user) => {
    commit('setUser', user)
  },
  setToken: ({ commit }, token) => {
    commit('setToken', token)
  }
}
