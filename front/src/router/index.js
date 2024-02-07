import Vue from 'vue';
import VueRouter from 'vue-router';
import LegalRequestForm from '../components/LegalRequestForm.vue';
import LegalRequestsDashboard from '../views/LegalRequestsDashboard.vue';

Vue.use(VueRouter);

const routes = [
  { path: '/submit-request', component: LegalRequestForm },
  { path: '/dashboard', component: LegalRequestsDashboard },
];

const router = new VueRouter({
  routes,
});

export default router;
