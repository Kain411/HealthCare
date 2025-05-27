import { createContext, useState } from "react";
import { register, login } from "../services/UserService";

export const UserContext = createContext()

export const UserProvider = ({children}) => {

    const [patient, setPatient] = useState({})

    const handleRegister = async (data) => {
        const result = await register(data)

        if (result.success) {
            setPatient(result.patient) 
        }

        return result
    }

    const handleLogin = async (data) => {
        const result = await login(data)

        if (result.success) {
            setPatient(result.patient)
        }

        return result
    }

    return (
        <UserContext.Provider value={{ patient, handleRegister, handleLogin }}>
            {children}
        </UserContext.Provider>
    )
}