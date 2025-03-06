import {defineStore} from 'pinia';
import type {User} from "~/types/user";

export interface UserPayloadInterface {
    email: string;
    password: string;
}

const authAPI = 'http://localhost:8000/api/auth';
const TWO_MIN = 2 * 60 * 1000;

export const useAuthStore = defineStore('auth', {
    state: () => {
        const isAuthenticated = isStoredTokenValid();
        console.log("LOGAN is auth", isAuthenticated);
        return {
            isAuthenticated: isAuthenticated,
            user: null as User | null,
        }
    },
    actions: {
        getStoredToken(): string | null | undefined {
            const token = useCookie('token');
            return token.value;
        },
        setStoredToken(value: string | null) {
            const token = useCookie('token');
            token.value = value;
        },
        async authenticateUser({email, password}: UserPayloadInterface) {
            try {
                const response: any = await useFetch(`${authAPI}/login`, {
                    method: 'post',
                    headers: {'Content-Type': 'application/json'},
                    body: {
                        email,
                        password,
                    },
                });
                const data = response.data.value;
                if (data) {
                    this.setStoredToken(data.token.access)
                    this.isAuthenticated = true;
                    this.user = data.user;
                    navigateTo('/home');
                }
            } catch (error) {
                console.error(error);
            }
        },
        logoutUser() {
            this.setStoredToken(null);
            const token = useCookie('token'); // useCookie new hook in nuxt 3
            this.isAuthenticated = false; // set authenticated  state value to false
            token.value = null; // clear the token cookie
            this.user = null; // clear the user state value
            navigateTo('/auth/login');
        }
    },
});

function isStoredTokenValid() {
    const tokenData = decodePayload();
    if (!tokenData.exp) {
        return null;
    }
    const expiresAt = tokenData.exp * 1000;
    const now = Date.now();
    return now + TWO_MIN < expiresAt;
}

function decodePayload(jwt?: string) {
    if (!jwt) {
        const storedJwt = useCookie('token');
        jwt = storedJwt.value || '';
    }
    const payload64 = jwt.split('.').at(1);
    const payload = payload64 ? atob(payload64) : '{}';
    const parsed = JSON.parse(payload);
    return parsed;
}