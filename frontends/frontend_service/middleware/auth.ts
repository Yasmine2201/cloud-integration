import {defineNuxtRouteMiddleware} from 'nuxt/app'
import {useAuthStore} from "~/store/auth";

export default defineNuxtRouteMiddleware((to, from) => {
    const authStore = useAuthStore();

    const isAuthenticated = authStore.isAuthenticated;
    const isInLoginPage = to.path.startsWith("/auth/");

    if (!isAuthenticated && !isInLoginPage) {
        return navigateTo('/auth/login');
    }
    if (isAuthenticated && isInLoginPage) {
        return navigateTo('/home');
    }
})
