// SignIn.js
import React, { useState } from 'react';
import "./Signin.css"



const SignIn = () => {
  const [phone, setPhone] = useState('');
  const [password, setPassword] = useState('');

  const handleSignIn = (e) => {
    e.preventDefault();
    // Add your authentication logic here (e.g., call an authentication API)
    console.log('Signing in with:', phone, password);
  };

  return (
    <div className="signin-container  mb-5">
      <h2>Sign In</h2>
      <form onSubmit={handleSignIn}>
        <div className="mb-3">
          <label htmlFor="phone" className="form-label">phone</label>
          <input
            type="phone"
            className="form-control"
            id="phone"
            placeholder="Enter your phone Number"
            value={phone}
            onChange={(e) => setPhone(e.target.value)}
            required
          />
        </div>
        <div className="mb-3">
          <label htmlFor="password" className="form-label">Password</label>
          <input
            type="password"
            className="form-control"
            id="password"
            placeholder="Enter your password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
        </div>
        <button type="submit" className="btn btn-primary">Sign In</button>
      </form>
    </div>
  );
};

export default SignIn;
