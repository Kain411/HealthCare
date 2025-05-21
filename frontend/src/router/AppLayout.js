import { BrowserRouter, Routes, Route } from 'react-router-dom'
import ContextWrapper from '../context/ContextWrapper'
import Header from '../pages/include/Header'
import Home from '../pages/Home'
import Appointment from '../pages/Appointment'
import AppointmentDetail from '../pages/AppointmentDetail'
import MedicalRecord from '../pages/MedicalRecord'
import Prescription from '../pages/Prescription'
import Predict from '../pages/Predict'
import Profile from '../pages/Profile'

const AppLayout = () => {
    return (
        <ContextWrapper>
            <BrowserRouter>
                <Routes>
                    <Route path='/' element={<Header />} >
                        <Route path='/home' element={<Home />} />
                        <Route path='/appointment' element={<Appointment />} />
                        <Route path='/appointment/details' element={<AppointmentDetail />} />
                        <Route path='/medical_record' element={<MedicalRecord />} />
                        <Route path='/prescription' element={<Prescription />} />
                        <Route path='/predict' element={<Predict />} />
                        <Route path='/profile' element={<Profile />} />
                    </Route>
                </Routes>
            </BrowserRouter>
        </ContextWrapper>
    )
}

export default AppLayout;