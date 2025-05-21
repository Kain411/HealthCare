import { Host } from './Host'
const API = `${Host}/medical_records`

export const getMedicalRecordsByPatientID = async (patientID) => {
    try {
        const response = await fetch(`${API}/${patientID}`)
        
        if (!response.ok) {
            return { "success": false, "error": "Error API" }
        }

        return await response.json()
    }
    catch (error) {
        return { "success": false, "error": "Error: getMedicalRecordsByPatientID" }
    }
}