import { createContext, useState } from "react";
import { getPrescriptionsByPatientID } from "../services/PrescriptionService";

export const PrescriptionContext = createContext()

export const PrescriptionProvider = ({children}) => {

    const [prescriptions, setPrescriptions] = useState({})

    const handlGetPrescriptionsByPatientID = async (patientID) => {
        const result = await getPrescriptionsByPatientID(patientID)

        if (result.success) {
            setPrescriptions(result.prescriptions)
        }

        return result
    }

    return (
        <PrescriptionContext.Provider value={{ prescriptions, handlGetPrescriptionsByPatientID }}>
            {children}
        </PrescriptionContext.Provider>
    )
}