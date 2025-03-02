import {defineNuxtRouteMiddleware} from 'nuxt/app'
import {useAuthStore} from "~/store/auth";

export default defineNuxtRouteMiddleware((to, from) => {
    const authStore = useAuthStore();
    if (!authStore.isAuthenticated && to.path !== '/login') {
        return navigateTo('/login');
    }
    const token = useCookie('token');
    if (token.value && from?.name === 'login') {
        return navigateTo('/home');
    }



})
