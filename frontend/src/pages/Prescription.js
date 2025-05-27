import { useContext, useEffect } from "react"
import "./style/Prescription.css"
import { PrescriptionContext } from "../context/PrescriptionContext"
import { UserContext } from "../context/UserContext"

const PrescriptionComponent = ({data}) => {
    return (
        <div className="prescription_form">
            {/* <div className="56556center" */}knk
        </div>
    )
}

const Prescription = () => {

    const { patient } = useContext(UserContext)
    const { prescriptions, handlGetPrescriptionsByPatientID } = useContext(PrescriptionContext)

    useEffect(() => {
        const getInfo = async () => {
            const result = await handlGetPrescriptionsByPatientID(patient.id)
        }
        getInfo()
    }, [])

    return (
        <div className="prescription_container">
            {
                prescriptions.map((data, index) => {
                    return <PrescriptionComponent key={index} data={data} />
                })
            }
        </div>
    )
}

export default Prescription;