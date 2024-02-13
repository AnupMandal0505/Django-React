/* src/index.css or src/index.scss */
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap.min.js";
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

import Home from "./pages/Home"
import Navbar from "./components/Navbar";
import About from "./pages/About";
import Contact from "./pages/Contact";
import Footer from "./components/Footer/Footer"
import Signup from "./pages/Register/UserRegister";
import SignIn from "./pages/Auth/Signin";
import Table from "./pages/Table";
import Dashboard from "./pages/Dashboard/Base.jsx"

import Layout from "./pages/Dashboard/Layout.jsx";
function App() {

  const userData = {
    name:"Anurag",
    age:21,
  };

  return (

    <Router>
    {/* <Navbar /> */}
    <Routes>
      <Route path="/" exact element={<Home user={userData} />} />
      <Route path="/about" element={<About />} />
      <Route path="/Contact" element={<Contact />} />
      <Route path="/Signup" element={<Signup />} />
      <Route path="/SignIn" element={<SignIn />} />
      <Route path="/Table" element={<Table />} />
      <Route path="/Layout" element={<Layout />} />
    </Routes>
    {/* <Footer /> */}
  </Router>
  )
}

export default App
