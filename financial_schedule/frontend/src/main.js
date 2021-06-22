import Vue from "vue";
import App from "./App.vue";
import router from "./router";

import VCalendar from 'v-calendar';
import { BootstrapVue } from 'bootstrap-vue'

// Import Bootstrap an BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'


Vue.config.productionTip = false;

Vue.use(BootstrapVue)
// Use v-calendar & v-date-picker components
Vue.use(VCalendar, {
  componentPrefix: 'vc',
  screens: {
    tablet: '576px',
    laptop: '992px',
    desktop: '1200px',
  },
});

new Vue({
  router,
  render: (h) => h(App),
}).$mount("#app");
