import { Host } from "./Host"
const API = `${Host}/doctors`

export const getDoctors = async () => {
    try {
        const response = await fetch(`${API}`)

        if (!response.ok) {
            return { "success": false, "error": "Error API" }
        }

        return await response.json()
    }
    catch (error) {
        return { "succes": false, "error": "Error: getDoctors" }
    }
}

export const getDoctorByID = async (doctorID) => {
    try {
        const response = await fetch(`${API}/${doctorID}`)

        if (!response.ok) {
            return { "success": false, "error": "Error API" }
        }

        return await response.json()
    }
    catch (error) {
        return { "succes": false, "error": "Error: getDoctorByID" }
    }
}