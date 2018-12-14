import Vue from 'vue'
import Vuetify from 'vuetify'
import App from '@/App.vue'

import router from './router'
import store from './store'
import $backend from '@/backend'

import 'vuetify/dist/vuetify.min.css'

Vue.use(Vuetify)

Vue.prototype.$backend = $backend
Vue.config.productionTip = false

const vue = new Vue({
  router,
  store,
  render: h => h(App)
})

vue.$mount('#app')
