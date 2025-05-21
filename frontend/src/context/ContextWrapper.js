import { PatientProvider } from "./PatientContext";
import { DoctorProvider } from "./DoctorContext";
import { AppointmentProvider } from "./AppointmentContext";
import { PrescriptionProvider } from "./PrescriptionContext";
import { PredictProvider } from "./PredictContext";
import { MedicalRecordProvider } from "./MedicalRecordContext";

const ContextWrapper = ({children}) => {
    return (
        <PatientProvider>
            <DoctorProvider>
                <AppointmentProvider>
                    <PrescriptionProvider>
                        <MedicalRecordProvider>
                            <PredictProvider>
                                {children}
                            </PredictProvider>
                        </MedicalRecordProvider>
                    </PrescriptionProvider>
                </AppointmentProvider>
            </DoctorProvider>
        </PatientProvider>
    )
}

export default ContextWrapper;