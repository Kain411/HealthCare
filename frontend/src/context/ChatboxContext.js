import { createContext, useState } from "react";
import { getDiseases, getSymptoms } from "../services/ChatboxService";

export const ChatboxContext = createContext()

export const ChatboxProvider = ({children}) => {

    const [symptoms, setSymptoms] = useState([])
    const [lstChat, setLstChat] = useState([])

    const addChat = (content) => {
        setLstChat(prev => ([
            ...prev,
            content
        ]))
    }

    const handleGetSymptoms = async () => {
        const result = await getSymptoms()

        if (result.success) {
            setSymptoms(result.symptoms)
        }

        return result
    }

    const handleGetDiseases = async (data) => {
        const result = await getDiseases(data)

        return result;
    }

    return (
        <ChatboxContext.Provider value={{ symptoms, lstChat, addChat, handleGetSymptoms, handleGetDiseases }}>
            {children}
        </ChatboxContext.Provider>
    )
}