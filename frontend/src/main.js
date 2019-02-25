
//La app mas simple posible.
import Vue from 'vue'
import App from './components/App.vue'
import VueRouter from 'vue-router'

import './assets/app.css' //Añadimos css

import {routes} from './routes'
import {store} from './store/store'

Vue.use(VueRouter); //El momento que activo esto, se desconfigura todo.

const router = new VueRouter({
  mode: 'history',
  routes
});

new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App)
});


