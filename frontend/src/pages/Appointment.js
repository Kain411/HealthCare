import { useContext, useEffect } from "react"
import "./style/Appointment.css"
import { DoctorContext } from "../context/DoctorContext"
import { useNavigate } from "react-router-dom"
import { AppointmentContext } from "../context/AppointmentContext"
import { UserContext } from "../context/UserContext"

const AppointmentComponent = ({doctor}) => {

    const navigate = useNavigate()

    return (
        <button 
            className="button appointment_form center_x"
            onClick={() => navigate('/appointment/details', { state: {"doctor": doctor}})}
        >
            {
                doctor.gender=="Nam" ?
                <img src={require("../assets/doctorMale.png")} className="appointment_doctor_avatar" />
                : <img src={require("../assets/doctorFemale.png")} className="appointment_doctor_avatar" />
            }
            <p className="appointment_doctor_username">{doctor.username}</p>
            <hr />
            <div style={{textAlign: 'left'}}>
                <div className="appointment_doctor_info">Phone: {doctor.phone}</div>
                <div className="appointment_doctor_info">Specialties: {doctor.specialties}</div>
                <div className="appointment_doctor_info">License number: {doctor.licenseNumber}</div>
            </div>
        </button>
    )
}

const Appointment = () => {

    const { patient } = useContext(UserContext)
    const { doctors } = useContext(DoctorContext)
    const { handleGetAppointmentByPatientID } = useContext(AppointmentContext)

    useEffect(() => {
        const getInfo = async () => {
            const result = await handleGetAppointmentByPatientID(patient.id)
        }
        getInfo()
    }, [])
    
    return (
        <div className="appointment_container">
            {
                doctors.map((doctor, index) => {
                    return <AppointmentComponent key={index} doctor={doctor} />
                })
            }
        </div>
    )
}

export default Appointment;