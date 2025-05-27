import { PatientProvider } from "./PatientContext";
import { DoctorProvider } from "./DoctorContext";
import { AppointmentProvider } from "./AppointmentContext";
import { PrescriptionProvider } from "./PrescriptionContext";
import { PredictProvider } from "./PredictContext";
import { MedicalRecordProvider } from "./MedicalRecordContext";
import { ChatboxProvider } from "./ChatboxContext";
import { UserProvider } from "./UserContext";

const ContextWrapper = ({children}) => {
    return (
        <UserProvider>
            <PatientProvider>
                <DoctorProvider>
                    <AppointmentProvider>
                        <PrescriptionProvider>
                            <MedicalRecordProvider>
                                <ChatboxProvider>
                                    <PredictProvider>
                                        {children}
                                    </PredictProvider>
                                </ChatboxProvider>
                            </MedicalRecordProvider>
                        </PrescriptionProvider>
                    </AppointmentProvider>
                </DoctorProvider>
            </PatientProvider>
        </UserProvider>
    )
}

export default ContextWrapper;