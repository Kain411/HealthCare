import { BrowserRouter, Routes, Route } from 'react-router-dom'
import ContextWrapper from '../context/ContextWrapper'
import Header from '../pages/include/Header'
import Home from '../pages/Home'
import Appointment from '../pages/Appointment'
import AppointmentDetail from '../pages/AppointmentDetail'
import MedicalRecord from '../pages/MedicalRecord'
import Prescription from '../pages/Prescription'
import Tool from '../pages/Tool'
import Profile from '../pages/Profile'
import Login from '../pages/Login'
import Register from '../pages/Register'

const AppLayout = () => {
    return (
        <ContextWrapper>
            <BrowserRouter>
                <Routes>
                    <Route path='/' element={<Login />} />
                    <Route path='/register' element={<Register />} />
                    <Route path='/main' element={<Header />} >
                        <Route path='/main/home' element={<Home />} />
                        <Route path='/main/appointment' element={<Appointment />} />
                        <Route path='/main/appointment/details' element={<AppointmentDetail />} />
                        <Route path='/main/medical_record' element={<MedicalRecord />} />
                        <Route path='/main/prescription' element={<Prescription />} />
                        <Route path='/main/tool' element={<Tool />} />
                        <Route path='/main/profile' element={<Profile />} />
                    </Route>
                </Routes>
            </BrowserRouter>
        </ContextWrapper>
    )
}

export default AppLayout;