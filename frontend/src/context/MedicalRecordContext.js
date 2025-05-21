import { createContext, useState } from "react";
import { getMedicalRecordsByPatientID } from "../services/MedicalRecordService";

export const MedicalRecordContext = createContext()

export const MedicalRecordProvider = ({children}) => {
    
    const [medicalRecords, serMedicalRecords] = useState([])

    const handleGetMedicalRecordsByPatientID = async (patientID) => {
        const result = await getMedicalRecordsByPatientID(patientID)

        if (result.success) {
            serMedicalRecords(result.medical_records)
        }

        return result
    }

    return (
        <MedicalRecordContext.Provider value={{ medicalRecords, handleGetMedicalRecordsByPatientID }}>
            {children}
        </MedicalRecordContext.Provider>
    )
}