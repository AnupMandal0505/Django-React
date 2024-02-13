// components/Navbar.js
import React from 'react';
// import "../../components/Dasboard/Navbar.js"
const Navbar = ({setOpenSideBar}) => {
    
    return (
        <nav className="navbar navbar-expand-sm  navbar-light fixed-top" style={{ zIndex: "3", }}>
            <div className="container-fluid">
                <a className="navbar-brand" href="#" style={{paddingLeft:'55px', paddingRight:'130px',}}>
                    <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTXvmLn7mps-xlaWIf8U-CIAd8AiQony73Mg&usqp=CAU" alt="Avatar Logo" style={{ width: '40px' }} className="rounded-pill" />
                </a>

                <a href="#" className=" sidebar-toggler flex-shrink-0" onClick={()=>setOpenSideBar((prev)=>! prev)}>
                <span className="navbar-toggler-icon"></span>
                </a>        
                
                        
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#collapsibleNavbar">
                    <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse justify-content-end" id="collapsibleNavbar">
                    <ul className="navbar-nav">
                        <li className="nav-item">
                            <a className="nav-link" href="#">Message</a>
                        </li>
                        <li className="nav-item">
                            <a className="nav-link" href="#">Notification</a>
                        </li>
                        <li className="nav-item">
                            <a className="nav-link" href="#">Balance</a>
                        </li>
                        <li className="nav-item dropdown">
                            <a className="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">Account</a>
                            <ul className="dropdown-menu">
                                <li><a className="dropdown-item" href="#">Profile</a></li>
                                <li><a className="dropdown-item" href="#">Logout</a></li>
                            </ul>
                        </li>
                    </ul>
                </div>
            </div>
        </nav>
    );
};

export default Navbar;
