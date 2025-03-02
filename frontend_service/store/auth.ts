import {defineStore} from 'pinia';
import type {User} from "~/types/user";

export interface UserPayloadInterface {
    email: string;
    password: string;
}

export const useAuthStore = defineStore('auth', {
    state: () => ({
        isAuthenticated: false,
        user: null as User | null,
    }),
    actions: {
        async authenticateUser({email, password}: UserPayloadInterface) {
            try {
                const data: any = await useFetch('http://localhost:8000/api/auth/login', {
                    method: 'post',
                    headers: {'Content-Type': 'application/json'},
                    body: {
                        email,
                        password,
                    },
                });
                if (data.data.value) {
                    console.log("inside store", data);
                    const token = useCookie('token');
                    token.value = data?.value?.token.access; // set token to cookie
                    this.isAuthenticated = true; // set authenticated state value to true
                    this.user = data.user; // set user state value to user data
                    navigateTo('/home'); // navigate to home page
                }


            } catch (error) {
                console.error(error);

            }
        },
        logoutUser() {
            const token = useCookie('token'); // useCookie new hook in nuxt 3
            this.isAuthenticated = false; // set authenticated  state value to false
            token.value = null; // clear the token cookie
            this.user = null; // clear the user state value
            navigateTo('/');
        },
    },
});
