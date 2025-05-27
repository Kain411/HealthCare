import { useState } from "react";
import "./style/Tool.css"
import Predict from "./include/Predict";
import Chatbox from "./include/Chatbox";

const Tool = () => {

    const [tool, setTool] = useState("Chatbox")

    return (
        <div className="tool_container">
            <div className="tool_change">
                <div className="tool_title">
                    Công cụ
                </div>
                <button 
                    className="button tool_btn"
                    onClick={() => setTool("Chatbox")}
                >Chatbox</button>
                <button 
                    className="button tool_btn"
                    onClick={() => setTool("Predict")}
                >Chẩn đoán</button>
            </div>

            {
                tool==="Chatbox" ?
                <Chatbox />
                : 
                <Predict />
            }
        </div>
    )
}

export default Tool;