import { Host } from './Host'
const API = `${Host}/appointments`

export const getAppointmentsByDoctorID = async (doctorID) => {
    try {
        const response = await fetch(`${API}/${doctorID}`)

        if (!response.ok) {
            return { "success": false, "error": "Error API" }
        }

        return await response.json()
    }
    catch (error) {
        return { "success": false, "error": "Error: getAppointmentsByDoctorID" }
    }
}

export const getAppointmentsByPatientID = async (patientID) => {
    try {
        const response = await fetch(`${API}/patient/${patientID}`)

        if (!response.ok) {
            return { "success": false, "error": "Error API" }
        }

        return await response.json()
    }
    catch (error) {
        return { "success": false, "error": "Error: getAppointmentsByPatientID" }
    }
}

export const postNewAppointment = async (data) => {
    try {
        const response = await fetch(`${API}/newAppointment`, {
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
        return { "success": false, "error": "Error: postNewAppointment" }
    }
}

export const deleteAppointment = async (data) => {
    try {
        const response = await fetch(`${API}/deleteAppointment`, {
            method: 'DELETE',
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
        return { "success": false, "error": "Error: deleteAppointment" }
    }
}