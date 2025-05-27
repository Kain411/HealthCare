import { Outlet, useNavigate } from 'react-router-dom';
import '../style/Header.css'
import { useContext, useEffect, useRef } from 'react';
import { DoctorContext } from '../../context/DoctorContext';
import { ChatboxContext } from '../../context/ChatboxContext';
import { UserContext } from '../../context/UserContext';

const Header = () => {

    const navigate = useNavigate()

    const { patient } = useContext(UserContext)
    const { handleGetDoctors } = useContext(DoctorContext)
    const { addChat, handleGetSymptoms } = useContext(ChatboxContext)
    const hasInitialized = useRef(false)

    useEffect(() => {
        const getInfo = async () => {
            const resultDoctor = await handleGetDoctors()
            const resultSymptom = await handleGetSymptoms()
        }
        getInfo()
        if (!hasInitialized.current) addChat({
            "type": "Chat",
            "content": "Xin chào " + patient.username + " !"
        })
        hasInitialized.current = true
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
                        onClick={() => navigate('/main/home')}
                    >Trang chủ
                    </button>
                    
                    <button 
                        className='button header_button'
                        onClick={() => navigate('/main/appointment')}
                    >Hẹn khám
                    </button>

                    <button 
                        className='button header_button'
                        onClick={() => navigate('/main/medical_record')}
                    >Hồ sơ bệnh án
                    </button>

                    <button 
                        className='button header_button'
                        onClick={() => navigate('/main/prescription')}
                    >Đơn thuốc
                    </button>

                    <button 
                        className='button header_button'
                        onClick={() => navigate('/main/tool')}
                    >Công cụ
                    </button>

                    <button 
                        className='button header_button'
                        onClick={() => navigate('/main/profile')}
                    >Hồ sơ cá nhân
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