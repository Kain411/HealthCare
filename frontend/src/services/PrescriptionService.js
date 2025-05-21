import { Host } from './Host'
const API = `${Host}/prescriptions`

export const getPrescriptionsByPatientID = async (patientID) => {
    try {
        const response = await fetch(`${API}/${patientID}`)

        if (!response.ok) {
            return { "success": false, "error": "Error API" }
        }

        return await response.json()
    }
    catch (error) {
        return { "success": false, "error": "Error: getPrescriptionsByPatientID" }
    }
}