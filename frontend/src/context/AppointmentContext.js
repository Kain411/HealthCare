import { createContext, useState } from "react";
import { getAppointmentsByDoctorID, getAppointmentsByPatientID, postNewAppointment } from "../services/AppointmentService";

export const AppointmentContext = createContext()

export const AppointmentProvider = ({children}) => {

    const [myAppointment, setMyAppointment] = useState([])

    const handleGetAppointmentByDoctorID = async (doctorID) => {
        const result = await getAppointmentsByDoctorID(doctorID)

        return result
    }

    const handleGetAppointmentByPatientID = async (patientID) => {
        const result = await getAppointmentsByPatientID(patientID)

        if (result.success) {
            setMyAppointment(result.appointments)
        }
        else setMyAppointment([])

        return result
    }

    const handlePostNewAppointment = async (patientID, data) => {
        const result = await postNewAppointment(data)

        if (result.success) {
            await handleGetAppointmentByPatientID(patientID)
        }

        return result
    }

    return (
        <AppointmentContext.Provider value={{ myAppointment, handleGetAppointmentByDoctorID, handleGetAppointmentByPatientID, handlePostNewAppointment }}>
            {children}
        </AppointmentContext.Provider>
    )
}