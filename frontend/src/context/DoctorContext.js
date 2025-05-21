import { createContext, useState } from "react";
import { getDoctorByID, getDoctors } from "../services/DoctorService";

export const DoctorContext = createContext()

export const DoctorProvider = ({children}) => {

    const [doctors, setDoctors] = useState({})

    const handleGetDoctors = async () => {
        const result = await getDoctors()

        if (result.success) {
            setDoctors(result.doctors)
        }

        return result
    }

    const handleGetDoctorByID = async (doctorID) => {
        const result = await getDoctorByID(doctorID)

        return result
    }

    return (
        <DoctorContext.Provider value={{ doctors, handleGetDoctors, handleGetDoctorByID }}>
            {children}
        </DoctorContext.Provider>
    )
}