import Cookies from 'js-cookie';
import axios from 'axios';
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';



function Login() {
  const [user_name, setUsername] = useState('');
  const [password, setPassword] = useState('');
  
  const naviage = useNavigate();
  
  const handleLogin = async () => {
    try {
      const response = await axios.post('http://localhost:8000/login', { user_name, password });
      const { access_token } = response.data;
      Cookies.set('jwt', access_token, { expires: 1 });
      console.log(access_token)
      const redirectTo = Cookies.get('redirectTo');
      if (redirectTo){
        naviage(redirectTo);
      }
      else {
        naviage('/')
      }
      

    } catch (error) {
      alert('Invalid username or password');
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

    </div>
  );
}

export default Login;