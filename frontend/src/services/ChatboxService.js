import { Host } from "./Host"
const API = `${Host}/chats`

export const getSymptoms = async () => {
    try {
        const response = await fetch(`${API}/symptoms`)

        if (!response.ok) {
            return { "success": false, "error": "Error API" }
        }

        return await response.json()
    }
    catch (error) {
        return { "succes": false, "error": "Error: getSymptoms" }
    }
}

export const getDiseases = async (data) => {
    try {
        const response = await fetch(`${API}/predict`, {
            method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                "symptoms": data
            })
        })

        return await response.json()
    }
    catch (error) {
        return { "success": false, "error": "Error: getDiseases" }
    }
}