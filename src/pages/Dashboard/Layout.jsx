// components/Layout.js
import React, { useState } from 'react';
import Sidebar from '../../components/Dasboard/Sidebar';
import Navbar from '../../components/Dasboard/Navbar.jsx';
import MainContent from '../../components/Dasboard/MainContent';

const Layout = () => {
  const [openSideBar, setOpenSideBar] = useState(true);
  return (
    <div className="container-fluid">
      <div className="row">
        <Sidebar openSideBar={openSideBar}/>
        <div className="col">
          <Navbar setOpenSideBar={setOpenSideBar} />

          <MainContent OpenMainContent={openSideBar}/>
        </div>
      </div>
    </div>
  );
};

export default Layout;
