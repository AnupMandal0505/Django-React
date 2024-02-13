import { useContext, useEffect, useState } from "react";
// import UserData from "./components/UserData.jsx";
import Data from "../components/Pagination/Data";
import { AppContext } from "../useContext/useContext";

const API = "http://127.0.0.1:8000/api/getalluser/";

const Table = () => {
    const [users, setUsers] = useState([]);

    const data= useContext(AppContext);

    // let isLoading = true;

    const fetchUsers = async (url) => {
        try {
            const res = await fetch(url);
            const data = await res.json();
            if (data.length > 0) {
                setUsers(data);
            }
            // isLoading=false;
            // console.log(data);
        } catch (e) {
            console.error(e)
        }
    }


    useEffect(() => {
        fetchUsers(API);
    }, [])

    // if (isLoading) {
    //     return (<>
    //         <h1>Loading....</h1>
    //     </>
    //     );
    // }
    return <>

        <div className="container mb-5" style={{ marginTop: '100px' }}>
            <h1>{data}</h1>
            <table className="table ">
                <thead className="table-dark">
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Phone</th>
                        <th>Email</th>
                        <th>Age</th>

                    </tr>
                </thead>
                <tbody>
                    <Data users={users} />

                </tbody>
            </table>
        </div>
    </>
}

export default Table;