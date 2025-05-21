import { createContext, useState } from "react";
import { getPatientByUsername, postNewPatient } from "../services/PatientService";

export const PatientContext = createContext()

export const PatientProvider = ({children}) => {

    const [patient, setPatient] = useState({})

    const handleGetPatientByUsername = async (username) => {
        const result = await getPatientByUsername(username)

        if (result.success) {
            setPatient(result.patient) 
        }

        return result
    }

    const handlePostNewPatient = async (data) => {
        const result = await postNewPatient(data)

        if (result.success) {
            setPatient(result.patient)
        }

        return result
    }

    return (
        <PatientContext.Provider value={{ patient, handleGetPatientByUsername, handlePostNewPatient }}>
            {children}
        </PatientContext.Provider>
    )
}