import { useContext, useState } from "react";
import "../style/Predict.css"
import { PredictContext } from "../../context/PredictContext";

const Form1 = ({title, value, field, handleChange}) => {

    return (
        <div className="predict_form">
            <p className="predict_content">{title}:</p>
            <input 
                type="text" 
                className="input predict_input" 
                value={value}
                onChange={(e) => handleChange(`${field}`, e.target.value)}
            />
        </div>
    )
}

const Form2 = ({title, value, field, handleChange}) => {
    return (
        <div className="predict_form">
            <p className="predict_content">{title}:</p>
            <div className="center_y predict_type">
                <div className="center_y">
                    <input 
                        type="radio" 
                        name={field}
                        value={value}
                        checked={value=="Có"}
                        onChange={() => handleChange(`${field}`, "Có")}
                    />
                    <span className="predict_choose">Có</span>
                </div>
                <div className="center_y">
                    <input 
                        type="radio" 
                        name={field} 
                        value={value}
                        checked={value=="Không"}
                        onChange={() => handleChange(`${field}`, "Không")}
                    />
                    <span className="predict_choose">Không</span>
                </div>
            </div>
        </div>
    )
}

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
                    <Form1 title={"Tuổi"} value={info.age} field={"age"} handleChange={handleChange} />
                    <Form1 title={"Giới tính"} value={info.gender} field={"gender"} handleChange={handleChange} />
                    <Form1 title={"Nhịp tim"} value={info.heartRate} field={"heartRate"} handleChange={handleChange} />
                    <Form1 title={"Huyết áp"} value={info.bloodPressure} field={"bloodPressure"} handleChange={handleChange} />
                </div>
                <div className="predict_body">
                    <Form2 title={"Sốt"} value={info.fever} field={"fever"} handleChange={handleChange} />
                    <Form2 title={"Ho"} value={info.cough} field={"cough"} handleChange={handleChange} />
                    <Form2 title={"Tức ngực"} value={info.chestPain} field={"chestPain"} handleChange={handleChange} />
                    <Form2 title={"Khó thở"} value={info.breath} field={"breath"} handleChange={handleChange} />
                    <Form2 title={"Chóng mặt"} value={info.dizzy} field={"dizzy"} handleChange={handleChange} />
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