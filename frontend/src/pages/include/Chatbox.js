import { useContext, useState } from "react";
import "../style/Chatbox.css"
import { ChatboxContext } from "../../context/ChatboxContext";

const Chatbox = () => {

    const { symptoms, lstChat, addChat, handleGetDiseases } = useContext(ChatboxContext)

    const [display, setDisplay] = useState(false)
    const [lstSymptoms, setLstSymptoms] = useState([])

    const handleAddSymptom = (symptom) => {
        setLstSymptoms(prev => ([
            ...prev,
            symptom
        ]))
    }

    const handleRemoveSymptom = (symptom) => {
        const res = []
        for (const item of lstSymptoms) {
            if (item!==symptom) res.push(item)
        }
        setLstSymptoms(res)
    }

    const handleSend = async () => {
        if (lstSymptoms.length==0) {
            alert("Bạn chưa thêm triệu chứng nào")
        }
        else {
            let mess = "Triệu chứng của bạn:" + '\n';
            for (const sym of lstSymptoms) {
                mess += sym + '\n'
            }
            addChat({
                "type": "User",
                "content": mess
            })
            const result = await handleGetDiseases(lstSymptoms)
            addChat({
                "type": "Chat",
                "content": result.message
            })
            setDisplay(false)
        }
    }

    return (
        <div className="chatbox_container">
            <div className="chatbox_title">Chatbox</div>
            <div className="chatbox_main">
                {
                    lstChat.map((item, index) => (
                        item.type=="Chat" ?
                        <div key={index} className="chat_wrapper_chat">
                            <div className="chat_form_chat">{item.content}</div>
                        </div>
                        :
                        <div key={index} className="chat_wrapper_user">
                            <div className="chat_form_user">{item.content}</div>
                        </div>
                    ))
                }
            </div>
            <div className="chatbox_footer center_y space_between">
                <input 
                    type="text"
                    className="chatbox_input"
                    placeholder="Nội dung của bạn..."
                />
                <button 
                    className="button chatbox_add_symptom"
                    onClick={() => setDisplay(true)}
                >   
                    {lstSymptoms.length==0 ? "Thêm" : lstSymptoms.length + " triệu chứng"}
                </button>
                <button 
                    className="button chatbox_send"
                    onClick={() => handleSend()}
                >
                    Gửi
                </button>
            </div>
            {
                display &&
                <div className="chatbox_symptoms">
                    {
                        symptoms.map((symptom, index) => {
                            return (
                                <div key={index} className="chatbox_symptom center_y">
                                    {
                                        lstSymptoms.includes(symptom) ?
                                        <button 
                                            className="button chatbox_choose_btn"
                                            onClick={() => handleRemoveSymptom(symptom)}
                                        >
                                            <img src={require("../../assets/check.png")} className="chatbox_choose_symptom" />
                                        </button>
                                        :
                                        <button 
                                            className="button chatbox_choose_btn"
                                            onClick={() => handleAddSymptom(symptom)}
                                        >
                                            <img src={require("../../assets/unCheck.png")} className="chatbox_choose_symptom" />
                                        </button>
                                    }
                                    <div className="chatbox_choose_content">{symptom}</div>
                                </div>
                            )
                        })
                    }
                </div>
            }
        </div>
    )
}

export default Chatbox;