// components/Sidebar.js
import React from 'react';
import "./Sidebar.css"
const Sidebar = ({openSideBar}) => {
    return (
        <nav className= {`col-md-2 d-none d-md-block ${openSideBar?'sidebar':'sidebar-active'}`}  >
            <div className="sidebar-sticky">
                <a className="navbar-brand" href="#">Dashboard</a>
                <ul className="nav flex-column">
                    <li className="nav-item">
                        <div className="d-flex  text-white">
                            <div > <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTXvmLn7mps-xlaWIf8U-CIAd8AiQony73Mg&usqp=CAU" alt="Avatar Logo" style={{ width: '40px' }} className="rounded-pill" /></div>
                            <a className="nav-link " href="#">Wc</a>
                        </div>
                    </li>
                    <li className="nav-item">
                        <div className="d-flex  text-white">
                            <div> <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTXvmLn7mps-xlaWIf8U-CIAd8AiQony73Mg&usqp=CAU" alt="Avatar Logo" style={{ width: '40px' }} className="rounded-pill" /></div>
                            <div className="p-1">
                                <a className="nav-link " href="#">
                                    SWC
                                </a>
                            </div>
                        </div>
                    </li>
                    <li className="nav-item">
                        <div className="d-flex  text-white">
                            <div > <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTXvmLn7mps-xlaWIf8U-CIAd8AiQony73Mg&usqp=CAU" alt="Avatar Logo" style={{ width: '40px' }} className="rounded-pill" /></div>
                            <div className="p-1">
                                <a className="nav-link " href="#">
                                    DWC
                                </a>
                            </div>
                        </div>
                    </li>
                    <li className="nav-item">
                        <div className="d-flex  text-white">
                            <div> <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTXvmLn7mps-xlaWIf8U-CIAd8AiQony73Mg&usqp=CAU" alt="Avatar Logo" style={{ width: '40px' }} className="rounded-pill" /></div>
                            <div className="p-1">
                                <a className="nav-link " href="#">
                                    Profile
                                </a>
                            </div>
                        </div>
                    </li>
                    <li className="nav-item">
                        <div className="d-flex  text-white">
                            <div > <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTXvmLn7mps-xlaWIf8U-CIAd8AiQony73Mg&usqp=CAU" alt="Avatar Logo" style={{ width: '40px' }} className="rounded-pill" /></div>
                            <div className="p-1">
                                <a className="nav-link " href="#">
                                    Setting
                                </a>
                            </div>
                        </div>
                    </li>
                    <li className="nav-item">
                        <div className="d-flex text-white">
                            <div > <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTXvmLn7mps-xlaWIf8U-CIAd8AiQony73Mg&usqp=CAU" alt="Avatar Logo" style={{ width: '40px' }} className="rounded-pill" /></div>
                            <div className="p-1">
                                <a className="nav-link " href="#">
                                    Logout
                                </a>
                            </div>
                        </div>
                    </li>

                    {/* Add more sidebar items as needed */}
                </ul>
            </div>
        </nav>
    );
};

export default Sidebar;
