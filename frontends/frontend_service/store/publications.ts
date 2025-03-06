import {defineStore} from 'pinia';

export type Publications = Publication[]

export interface Publication {
  id: number
  number_likes: number
  has_user_liked: boolean
  title: string
  body: string
  created_at: string
  publisher: number
}

const publicationsAPI = 'http://localhost:8001/api/publications';

export const usePublicationsStore = defineStore('publications', {
    state: () => {
        return {
            publications: [] as Publications,
            loaded: false,
        }
    },
    actions: {
        getAuth(): string {
            const token = useCookie('token');
            return token.value ? `Bearer ${token.value}` : '';
        },
        async loadData() {
            try {
                const response: any = await useFetch(`${publicationsAPI}/`, {
                    method: 'get',
                    headers: {'Content-Type': 'application/json', 'Authorization': this.getAuth()}
                });
                const data = response.data.value;
                if (data) {
                    console.log("logan", {data});
                }
                this.loaded = true;
            } catch (error) {
                console.error(error);
            }
        }
    },
});
