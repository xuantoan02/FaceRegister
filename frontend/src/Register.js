import { useForm } from 'react-hook-form';
import axios from 'axios';
import React from 'react';
import { useNavigate } from 'react-router-dom';


function Register() {
  const { register, handleSubmit, formState: { errors } } = useForm();
  const naviage = useNavigate();
  const onSubmit = async (data) => {
    try {
      const response = await axios.post('http://localhost:8000/register', data);
      console.log(response.data)
      naviage('/Login');
      alert(response.data.message);
    } catch (error) {
      alert('An error occurred');
    }
  };

  return (
    <div>
      <h1>User Registration</h1>
      <form onSubmit={handleSubmit(onSubmit)}>
        <div>
          <label>Username</label>
          <input {...register('user_name', { required: true, minLength: 3, maxLength: 20 })} />
          {errors.username && <span>Username is required and must be between 3 and 20 characters</span>}
        </div>
        <div>
          <label>Email</label>
          <input {...register('email', { required: true, minLength: 3, maxLength: 20 })} />
          {errors.email && <span>Username is required and must be between 3 and 20 characters</span>}
        </div>

        <div>
          <label>Password</label>
          <input {...register('password', { required: true, minLength: 6 })} />
          {errors.password && <span>Password is required and must be at least 6 characters</span>}
        </div>
        <div>
          <button type="submit">Register</button>
        </div>
      </form>
    </div>
  );
}

export default Register;