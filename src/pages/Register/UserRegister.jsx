// Signup.js
import React, { useState } from 'react';
import "./UserRegister.css"

const Signup = () => {
  const [formData, setFormData] = useState({
    phone: '',
    email: '',
    password: '',
  });

  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value,
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      setLoading(true);
      setError('');

      const response = await fetch('http://127.0.0.1:8000/api/registerUser/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
      });

      if (!response.ok) {
        throw new Error('Network response was not ok');
      }

      const data = await response.json();
      console.log('Data received:', data);
    } catch (error) {
      console.error('Error during form submission:', error.message);
      setError('An error occurred during registration. Please try again.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="signup-container mb-5">
      <h2>Sign Up</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Phone:
          <input type="text" name="phone"  autoComplete="phone" value={formData.phone} onChange={handleChange} />
        </label>
        <label>
          Email:
          <input type="email" name="email" autoComplete="email" value={formData.email} onChange={handleChange} />
        </label>
        <label>
          Password:
          <input type="password" name="password" autoComplete="current-password" value={formData.password} onChange={handleChange} />
        </label>
        {loading && <p>Loading...</p>}
        {error && <p className="error-message">{error}</p>}
        <button type="submit" disabled={loading}>Sign Up</button>
      </form>
    </div>
  );
};

export default Signup;
