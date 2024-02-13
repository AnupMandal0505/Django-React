import React, { useContext } from "react";

const AppContext = React.createContext();

const AppProvider = ({ children }) =>{
    return(
        <AppContext.Provider value={"Anurag"}>
            {children}
        </AppContext.Provider>
    );
};

// custom hook create
const GloablContext = () =>{
    return useContext(AppContext);
};

export { AppContext, AppProvider,GloablContext};
