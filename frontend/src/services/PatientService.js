import { Host } from './Host'
const API = `${Host}/patients`

export const getPatientByUsername = async (username) => {
    try {
        const response = await fetch(`${API}/username/${username}`)

        if (!response.ok) {
            return { "success": false, "error": "Error API" }
        }

        return await response.json()
    }
    catch (error) {
        return { "success": false, "error": "Error: getPatientByUsername" }
    }
}

export const postNewPatient = async (data) => {
    try {
        const response = await fetch(`${API}/newPatient`)

        if (!response.ok) {
            return { "success": false, "error": "Error API" }
        }

        return await response.json()
    }
    catch (error) {
        return { "success": false, "error": "Error: postNewPatient" }
    }
}