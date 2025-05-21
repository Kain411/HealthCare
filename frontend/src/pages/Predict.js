import { useContext, useState } from "react";
import "./style/Predict.css"
import { PredictContext } from "../context/PredictContext";

const Predict = () => {

    const { handlePredict } = useContext(PredictContext)

    const [predict, setPredict] = useState("")
    const [info, setInfo] = useState({
        "age": 18,
        "gender": "Nam",
        "fever": "Có",
        "chestPain": "Có",
        "breath": "Có",
        "cough": "Có",
        "dizzy": "Có",
        "bloodPressure": "",
        "heartRate": ""
    })

    const handleChange = (key, value) => {
        setInfo(prev => ({
            ...prev,
            [key]: value
        }))
    }

    const handleSend = async () => {
        console.log("In")
        const result = await handlePredict(info)
        console.log("Out")
        setPredict(result.predict)
    }

    return (
        <div className="predict_container">
            <div className="space_between">
                <div className="predict_body">
                    <div className="predict_form">
                        <p className="predict_content">Age</p>
                        <input 
                            type="text" 
                            className="input predict_input" 
                            value={info.age}
                            onChange={(e) => handleChange("age", e.target.value)}
                        />
                    </div>
                    
                    <div className="predict_form">
                        <p className="predict_content">Gender</p>
                        <input 
                            type="text" 
                            className="input predict_input"
                            value={info.gender}
                            onChange={(e) => handleChange("gender", e.target.value)}
                        />
                    </div>
                    
                    <div className="predict_form">
                        <p className="predict_content">Blood Pressure</p>
                        <input 
                            type="text" 
                            className="input predict_input" 
                            value={info.bloodPressure}
                            onChange={(e) => handleChange("bloodPressure", e.target.value)}
                        />
                    </div>
                    
                    <div className="predict_form">
                        <p className="predict_content">Heart Rate</p>
                        <input 
                            type="text" 
                            className="input predict_input" 
                            value={info.heartRate}
                            onChange={(e) => handleChange("heartRate", e.target.value)}
                        />
                    </div>

                </div>
                <div className="predict_body">
                    <div className="predict_form">
                        <p className="predict_content">Fever</p>
                        <div className="center_y predict_type">
                            <div className="center_y">
                                <input 
                                    type="radio" 
                                    name="fever" 
                                    value={info.fever}
                                    checked={info.fever=="Có"}
                                    onChange={() => handleChange("fever", "Có")}
                                />
                                <span className="predict_choose">Yes</span>
                            </div>
                            <div className="center_y">
                                <input 
                                    type="radio" 
                                    name="fever" 
                                    value={info.fever}
                                    checked={info.fever=="Không"}
                                    onChange={() => handleChange("fever", "Không")}
                                />
                                <span className="predict_choose">No</span>
                            </div>
                        </div>
                    </div>
                    
                    <div className="predict_form">
                        <p className="predict_content">Chest pain</p>
                        <div className="center_y predict_type">
                            <div className="center_y">
                                <input 
                                    type="radio" 
                                    name="chestPain" 
                                    value={info.chestPain}
                                    checked={info.chestPain=="Có"}
                                    onChange={() => handleChange("chestPain", "Có")}
                                />
                                <span className="predict_choose">Yes</span>
                            </div>
                            <div className="center_y">
                                <input 
                                    type="radio" 
                                    name="chestPain" 
                                    value={info.chestPain}
                                    checked={info.chestPain=="Không"}
                                    onChange={() => handleChange("chestPain", "Không")}
                                />
                                <span className="predict_choose">No</span>
                            </div>
                        </div>
                    </div>
                    
                    <div className="predict_form">
                        <p className="predict_content">Breath</p>
                        <div className="center_y predict_type">
                            <div className="center_y">
                                <input 
                                    type="radio" 
                                    name="breath" 
                                    value={info.breath}
                                    checked={info.breath=="Có"}
                                    onChange={() => handleChange("breath", "Có")}
                                />
                                <span className="predict_choose">Yes</span>
                            </div>
                            <div className="center_y">
                                <input 
                                    type="radio" 
                                    name="breath" 
                                    value={info.breath}
                                    checked={info.breath=="Không"}
                                    onChange={() => handleChange("breath", "Không")}
                                />
                                <span className="predict_choose">No</span>
                            </div>
                        </div>
                    </div>
                    
                    <div className="predict_form">
                        <p className="predict_content">Cough</p>
                        <div className="center_y predict_type">
                            <div className="center_y">
                                <input 
                                    type="radio" 
                                    name="cough" 
                                    value={info.cough}
                                    checked={info.cough=="Có"}
                                    onChange={() => handleChange("cough", "Có")}
                                />
                                <span className="predict_choose">Yes</span>
                            </div>
                            <div className="center_y">
                                <input 
                                    type="radio" 
                                    name="cough" 
                                    value={info.cough}
                                    checked={info.cough=="Không"}
                                    onChange={() => handleChange("cough", "Không")}
                                />
                                <span className="predict_choose">No</span>
                            </div>
                        </div>
                    </div>
                    
                    <div className="predict_form">
                        <p className="predict_content">Dizzy</p>
                        <div className="center_y predict_type">
                            <div className="center_y">
                                <input 
                                    type="radio" 
                                    name="dizzy" 
                                    value={info.dizzy}
                                    checked={info.dizzy=="Có"}
                                    onChange={() => handleChange("dizzy", "Có")}
                                />
                                <span className="predict_choose">Yes</span>
                            </div>
                            <div className="center_y">
                                <input 
                                    type="radio" 
                                    name="dizzy" 
                                    value={info.dizzy}
                                    checked={info.dizzy=="Không"}
                                    onChange={() => handleChange("dizzy", "Không")}
                                />
                                <span className="predict_choose">No</span>
                            </div>
                        </div>
                    </div>

                </div>

            </div>
            {
                predict!="" &&
                <div className="predict_result">{predict}</div> 
            }

            <button 
                className="button predict_send"
                onClick={handleSend}
            >
                Chuẩn đoán
            </button>
        </div>
    )
}

export default Predict;