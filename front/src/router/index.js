import Vue from 'vue';
import VueRouter from 'vue-router';
import LegalRequestForm from '../components/LegalRequestForm.vue';
import LegalRequestsDashboard from '../views/LegalRequestsDashboard.vue';

Vue.use(VueRouter);

const routes = [
  { path: '/submit-request', component: LegalRequestForm, meta: { requiresAuth: true, userRole: 'user' } },
  { path: '/dashboard', component: LegalRequestsDashboard, meta: { requiresAuth: true, userRole: 'admin' } },
  // ... other routes ...
];

const router = new VueRouter({
  routes,
});
router.beforeEach((to, from, next) => {
  const userRole = localStorage.getItem('userRole');

  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!userRole) {
      // User is not authenticated
      next('/');  // THIS SHOULD REDIRECT TO LOGIN FORM
    } else if (userRole === 'admin') {
      // Admin is trying to access login, redirect to dashboard
      next('/dashboard');
    } else if (userRole !== to.meta.userRole) {
      // User role doesn't match the required role for the route, redirect to appropriate route
      next({ path: userRole === 'admin' ? '/dashboard' : '/submit-request' });
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;
