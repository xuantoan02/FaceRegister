import { useForm } from 'react-hook-form';
import axios from 'axios';
import React, { useState } from 'react';


function Login() {
  const [user_name, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [accessToken, setAccessToken] = useState('');

  const handleLogin = async () => {
    try {
      const response = await axios.post('http://localhost:8000/login', { user_name, password });
      const { access_token } = response.data;
      setAccessToken(access_token);
    } catch (error) {
      alert('Invalid username or password');
    }
  };

  const handleProtected = async () => {
    try {
      const response = await axios.get('http://localhost:8000/protected', {
        headers: { Authorization: `Bearer ${accessToken}` }
      });
      alert(response.data.message);
    } catch (error) {
      alert('Invalid token');
    }
  };

  return (
    <div>
      <h1>Login</h1>
      <div>
        <label>Username</label>
        <input type="text" value={user_name} onChange={(e) => setUsername(e.target.value)} />
      </div>
      <div>
        <label>Password</label>
        <input type="password" value={password} onChange={(e) => setPassword(e.target.value)} />
      </div>
      <button onClick={handleLogin}>Login</button>
      <hr />
      <h2>Protected Route</h2>
      <button onClick={handleProtected} disabled={!accessToken}>Access Protected Route</button>
    </div>
  );
}

export default Login;