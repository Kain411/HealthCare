import { useNavigate } from "react-router-dom";
import "./style/Form.css"
import { useContext, useState } from "react";
import { UserContext } from "../context/UserContext";

const Register = () => {

    const navigate = useNavigate()
    const [user, setUser] = useState({
        username: "",
        username: "",
        password: "",
        accuracy: "",
        role: "Patient"
    })

    const handleChange = (key, value) => {
        setUser(prev => ({
            ...prev,
            [key]: value
        }))
    }

    const { handleRegister } = useContext(UserContext)
    const register = async () => {

        const result = await handleRegister(user)

        if (result.success) navigate("/main/home")
        alert("Alert: " + result.message)
    }

    return (
        <div className="form_container center">
            <div className="form_main center_x">
                <p className="form_title">Đăng ký</p>

                <div className="form_info">
                    <p className="form_info_title">Tên đăng nhập:</p>
                    <input 
                        type="username" 
                        placeholder="Nhập username..." 
                        className="form_info_input" 
                        value={user.username}
                        onChange={(e) => handleChange("username", e.target.value)}
                    />
                </div>

                <div className="form_info">
                    <p className="form_info_title">Mật khẩu:</p>
                    <input 
                        type="password" 
                        placeholder="Nhập mật khẩu..." 
                        className="form_info_input" 
                        value={user.password}
                        onChange={(e) => handleChange("password", e.target.value)}
                    />
                </div>

                <div className="form_info">
                    <p className="form_info_title">Nhập lại mật khẩu:</p>
                    <input 
                        type="password" 
                        placeholder="Nhập lại mật khẩu..." 
                        className="form_info_input" 
                        value={user.accuracy}
                        onChange={(e) => handleChange("accuracy", e.target.value)}
                    />
                </div>

                <button className="button form_btn_submit center" onClick={register}>Đăng ký</button>

               <div className="center form_navigation">
                    Bạn đã có tài khoản?
                    <button className="button form_btn_navigation center" onClick={() => navigate("/")}>Đăng nhập</button>
               </div>
            </div>
        </div>
    )
}

export default Register;