import Vue from 'vue';
import VueRouter from 'vue-router';
import LegalRequestForm from '../components/LegalRequestForm.vue';
import Dashboard from '../views/Dashboard.vue';

Vue.use(VueRouter);

const routes = [
  { path: '/submit-request', component: LegalRequestForm },
  { path: '/dashboard', component: Dashboard },
];

const router = new VueRouter({
  routes,
});

export default router;
