export default {
  isProgressStatus: (state, status) => {
    state.isProgressStatus = status
  },
  isLoggedIn: (state, auth) => {
    state.isLoggedIn = auth
  },
  setUser: (state, user) => {
    state.user = user
  },
  setToken: (state, token) => {
    state.token = token
  },
  clearAllData: (state) => {
    // clear all
    state.isProgressStatus = false
    state.isLoggedIn = false
    state.user = null
    state.token = null
  }
}
