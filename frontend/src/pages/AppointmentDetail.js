import { useContext, useEffect, useState } from "react";
import { useLocation } from "react-router-dom";
import { AppointmentContext } from "../context/AppointmentContext";
import { UserContext } from "../context/UserContext";

const AppointmentComponent = ({doctor}) => {

    return (
        <button 
            className="button appointment_form center_x"
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
                <div className="appointment_doctor_info">Location: {doctor.location}</div>
            </div>
        </button>
    )
}

const AppointmentTime = ({index, info, status}) => {

    const { patient } = useContext(UserContext)
    const { handlePostNewAppointment, handleDeleteAppointment } = useContext(AppointmentContext)

    const [check, setCheck] = useState(status)

    const handleCheck = async () => {

        const data = {
            "patientID": patient.id,
            "appointmentID": info.id
        }

        if (check) {
            const result = await handleDeleteAppointment(patient.id, data)
            if (result.success) setCheck(false)
        }
        else {
            const result = await handlePostNewAppointment(patient.id, data)
            if (result.success) setCheck(true)
        }
    }

    return (
        <div className="appointment_time_container">
            <button 
                className="button appointment_time_button"
                onClick={() => handleCheck()}
            >
                {
                    check ?
                    <img src={require("../assets/check.png")} className="appointment_check_box"/>
                    : <img src={require("../assets/unCheck.png")} className="appointment_check_box"/>
                }
            </button>
            <div className="appointment_time_title">Cuộc hẹn {index<10 ? "0" + index : index}</div>
            <div className="appointment_time_content">Thời gian: {info.time}</div>
            <div className="appointment_time_content">Ngày hẹn: {info.day}</div>
        </div>
    )
}

const AppointmentDetail = () => {

    const location = useLocation()
    const doctor = location.state?.doctor

    const [appointments, setAppointments] = useState([])

    const { myAppointment, handleGetAppointmentByDoctorID } = useContext(AppointmentContext)
    useEffect(() => {
        const getInfo = async () => {
            const result = await handleGetAppointmentByDoctorID(doctor?.id)
            setAppointments(result.appointments)
        }
        getInfo()
    }, [])

    return (
        <div className="appointment_container">
            <div className="appointment_details_doctor center_x">
                <AppointmentComponent doctor={doctor} />
            </div>
            <div className="appointment_details_main">
                {
                    appointments?.map((info, index) => {
                        let status = false;
                        myAppointment?.map((info_child, index_child) => {
                            if (info.id==info_child.id) {
                                status = true
                            }
                        })

                        return <AppointmentTime key={index} index={index+1} info={info} status={status} />
                    })
                }
            </div>
        </div>
    )
}

export default AppointmentDetail;