import { Outlet, useNavigate } from 'react-router-dom';
import '../style/Header.css'
import { useContext, useEffect } from 'react';
import { PatientContext } from '../../context/PatientContext';
import { DoctorContext } from '../../context/DoctorContext';
import { AppointmentContext } from '../../context/AppointmentContext';

const Header = () => {

    const navigate = useNavigate()

    const { patient, handleGetPatientByUsername } = useContext(PatientContext)
    const { handleGetDoctors } = useContext(DoctorContext)

    useEffect(() => {
        const getInfo = async () => {
            const resultPatient = await handleGetPatientByUsername("Tzei")
            const resultDoctor = await handleGetDoctors()
        }
        getInfo()
    }, [])

    return (
        <div className='container'>
            <header className='header_container'>
                <div className='space_between header_info'>
                    <div className='center_y header_app'>
                        <span className='header_title'>
                            App Name
                        </span>
                        <div className='header_search'>
                            <div className='search_form center_y'>
                                <input type='text' className='input search_input' />
                                <img src={require('../../assets/search.png')} className='icon icon_search' />
                            </div>
                        </div>
                    </div>
                    <div className='center_y'>
                        <span className='header_username'>{patient.username}</span>
                        <img src={require("../../assets/asa.jpg")} className='header_avatar' />
                    </div>
                </div>
                <div className='space_between'>
                    <button 
                        className='button header_button'
                        onClick={() => navigate('/home')}
                    >Home
                    </button>
                    
                    <button 
                        className='button header_button'
                        onClick={() => navigate('/appointment')}
                    >Appointment
                    </button>

                    <button 
                        className='button header_button'
                        onClick={() => navigate('/medical_record')}
                    >MedicalRecord
                    </button>

                    <button 
                        className='button header_button'
                        onClick={() => navigate('/prescription')}
                    >Prescription
                    </button>

                    <button 
                        className='button header_button'
                        onClick={() => navigate('/predict')}
                    >Predict
                    </button>

                    <button 
                        className='button header_button'
                        onClick={() => navigate('/profile')}
                    >Profile
                    </button>
                </div>
            </header>
            <div className='header_body'>
                <Outlet />
            </div>
        </div>
    )
}

export default Header;