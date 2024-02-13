import React from 'react'
import './Navbar.css'
import { Link } from 'react-router-dom';

const Navbar = () => {
  return (
    <div>
      <nav className="navbar navbar-expand-sm fixed-top">
        <div className="container-fluid">
          <a className="navbar-brand" href="#">
            <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRTXvmLn7mps-xlaWIf8U-CIAd8AiQony73Mg&usqp=CAU" alt="Avatar Logo" style={{ width: '40px' }} className="rounded-pill" />
          </a>

          <div className="collapse navbar-collapse justify-content-center" id="collapsibleNavbar">
            <ul className="navbar-nav">
            <li className="nav-item">
                <Link to="/" >Home</Link>
              </li>
              <li className="nav-item">
                <Link to="/Layout" >Dashboard</Link>
              </li>
              <li className="nav-item">
                <Link to="/">Services</Link>
              </li>
              <li className="nav-item">
                <Link to="/Table">Data</Link>
              </li>
              <li className="nav-item">
                <Link to="/Contact">Contact Us</Link>
              </li>
              <li className="nav-item">
                <Link to="/About">About</Link>
              </li>
              <li className="nav-item dropdown">
                <a className="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown">Account</a>
                <ul className="dropdown-menu" aria-labelledby="navbarDropdown">
                  <li>
                    <Link to="/Signup" className="dropdown-item">Sign Up</Link>
                  </li>
                  <li>
                    <Link to="/SignIn" className="dropdown-item">Sign In</Link>
                  </li>
                </ul>
              </li>
              
            </ul>
          </div>
          <button type="button" className="btn btn-primary">Consultation</button>
          <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#collapsibleNavbar">
            <span className="navbar-toggler-icon"></span>
          </button>
        </div>
      </nav>
    </div>
  )
}

export default Navbar
