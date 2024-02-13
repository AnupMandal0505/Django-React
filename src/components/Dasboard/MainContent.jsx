// components/MainContent.js
import React from 'react';
import Footer from '../Dasboard/Footer.jsx';

import "./MainContent.css"
const MainContent = ({OpenMainContent}) => {
  return (
    <main className={`main-content mt-5 pt-5 ${OpenMainContent?'main-content':'main-content-active'}`}>
        <h1 className="h2"><ul>Dashboard</ul> </h1>
        <div className="container">
          <div className="row">
          <p>Lorem ipsum dolor sit, amet consectetur adipisicing elit. Suscipit doloremque iure provident, inventore ea minus. Asperiores expedita odit in mollitia velit? Officiis dolor tenetur iure et distinctio illo totam recusandae. Aliquam commodi eius itaque dolores accusantium dolore et neque dignissimos! Molestias dolor rem, alias consectetur quam neque officiis magni est!</p>

          </div>
        </div>
      <Footer />
    </main>
  );
};

export default MainContent;
