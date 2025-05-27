import { Host } from './Host'
const API = `${Host}/users`

export const register = async (data) => {
    try {
        const response = await fetch(`${API}/register`, {
            method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        })

        if (!response.ok) {
            return { "success": false, "error": "Error API" }
        }

        return await response.json()
    }
    catch (error) {
        return { "success": false, "error": "Error: Register" }
    }
}

export const login = async (data) => {
    try {
        const response = await fetch(`${API}/login`, {
            method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        })

        if (!response.ok) {
            return { "success": false, "error": "Error API" }
        }

        return await response.json()
    }
    catch (error) {
        return { "success": false, "error": "Error: Login" }
    }
}