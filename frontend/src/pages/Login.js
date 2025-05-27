import { useContext, useState } from "react";
import "./style/Form.css"
import { useNavigate } from "react-router-dom";
import { UserContext } from "../context/UserContext";

const Login = () => {

    const navigate = useNavigate()

    const [user, setUser] = useState({
        username: "",
        password: "",
        role: "Patient"
    })

    const handleChange = (key, value) => {
        setUser(prev => ({
            ...prev,
            [key]: value
        }))
    }

    const { handleLogin } = useContext(UserContext)
    const login = async () => {

        const result = await handleLogin(user)

        if (result.success) navigate("/main/home")
        alert("Alert: " + result.message)
    }

    return (
        <div className="form_container center">
            <div className="form_main center_x">
                <p className="form_title">Đăng nhập</p>

                <div className="form_info">
                    <p className="form_info_title">Tài đăng nhập:</p>
                    <input 
                        type="" 
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

                <button className="button form_btn_submit center" onClick={login}>Đăng nhập</button>

               <div className="center form_navigation">
                    Bạn chưa có tài khoản?
                    <button className="button form_btn_navigation center" onClick={() => navigate("/register")}>Đăng ký</button>
               </div>

               <button className="button form_btn_forget center">Quên mật khẩu?</button>
            </div>
        </div>
    )
}

export default Login;