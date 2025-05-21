import { createContext } from "react";
import { predict } from "../services/PredictService";

export const PredictContext = createContext()

export const PredictProvider = ({children}) => {

    const handlePredict = async (data) => {
        const result = predict(data)

        return result
    }

    return (
        <PredictContext.Provider value={{ handlePredict }}>
            {children}
        </PredictContext.Provider>
    )
}