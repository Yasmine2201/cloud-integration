export const apis = {
    get auth() {
        return window.location.port === '3000'
            ? 'http://localhost:8000/api/auth'
            : '/api/auth';
    },
    get publication() {
        return window.location.port === '3000'
            ? 'http://localhost:8001/api/publications'
            : '/api/publications';
    },
    get profile() {
        return window.location.port === '3000'
            ? 'http://localhost:8002/api/profile'
            : '/api/profile';
    }
}

