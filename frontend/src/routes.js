import Home from './components/Home.vue';
import Testing from './components/Testing.vue';



export const routes = [
  {path: '/', component: Home, name: 'home'},
    {path: '/test', component: Testing, name: 'test'}

      ]