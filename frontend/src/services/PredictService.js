import { Host } from './Host'
const API = `${Host}/predicts`

export const predict = async (data) => {
    try {
        const response = await fetch(`${API}`, {
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
        return { "success": false, "error": "Error: predict" }
    }
}