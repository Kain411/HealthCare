import { useContext, useEffect } from "react";
import "./style/MedicalRecord.css"
import { PatientContext } from "../context/PatientContext";
import { MedicalRecordContext } from "../context/MedicalRecordContext";

const MedicalRecordComponent = ({medicalRecord}) => {
    return (
        <div className="medical_record_form center_x">
            <div className="center_y">
                <div className="medical_record_user">
                    {
                        medicalRecord.doctor.gender=="Male" ?
                        <img src={require("../assets/doctorMale.png")} className="appointment_doctor_avatar" />
                        : <img src={require("../assets/doctorFemale.png")} className="appointment_doctor_avatar" />
                    }
                    <div className="medical_record_name">{medicalRecord.doctor.username}</div>
                    <div className="medical_record_phone">{medicalRecord.doctor.phone}</div>
                </div>
                <div className="medical_record_space"></div>
                <div className="medical_record_user">
                    {
                        medicalRecord.nurse.gender=="Male" ?
                        <img src={require("../assets/doctorMale.png")} className="appointment_doctor_avatar" />
                        : <img src={require("../assets/doctorFemale.png")} className="appointment_doctor_avatar" />
                    }
                    <div className="medical_record_name">{medicalRecord.nurse.username}</div>
                    <div className="medical_record_phone">{medicalRecord.nurse.phone}</div>
                </div>
            </div>
            <div className="medical_records_result">
                <p className="medical_records_content">{medicalRecord.note}</p>
                <p className="medical_records_content">{medicalRecord.result}</p>
            </div>
        </div>
    )
}

const MedicalRecord = () => {

    const { patient } = useContext(PatientContext)
    const { medicalRecords, handleGetMedicalRecordsByPatientID } = useContext(MedicalRecordContext)

    useEffect(() => {
        const getInfo = async () => {
            const result = await handleGetMedicalRecordsByPatientID(patient.id)
        }
        getInfo()
    }, [])

    return (
        <div className="medical_records_container">
            {
                medicalRecords?.map((medicalRecord, index) => {
                    return <MedicalRecordComponent key={index} medicalRecord={medicalRecord} />
                })
            }
        </div>
    )
}

export default MedicalRecord;