import Vue from 'vue'
import Router from 'vue-router'
import urls from './urls'

import Main from '../views/Main'
import Home from '../views/Home'

import SignUp from '../views/authentication/SignUp'
import Error404Page from '../views/404'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: urls.signup,
      name: 'signup',
      component: SignUp
    },
    {
      path: urls.index,
      component: Main,
      children: [
        {
          path: '',
          name: 'home',
          component: Home
        },
        {
          path: urls['404'],
          name: '404',
          component: Error404Page
        }
      ]
    }
  ]
})
