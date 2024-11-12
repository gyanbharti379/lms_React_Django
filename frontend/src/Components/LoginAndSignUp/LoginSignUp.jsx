import React from 'react'
import './loginSignup.css'
import axios from 'axios'
import { redirect } from 'react-router-dom';
 
const LoginSignupComponent = () => {
    const [isLogin, setIsLogin] = React.useState(true);
    const [email,setEmail]=React.useState()
    const [password,setPassword]=React.useState()

    const handleSubmit = () => {
      const payload = {
        email: email,
        password: password,
      }
        console.log(payload);
      axios.post('http://127.0.0.1:8000/user/api/user/login', payload)
      .then(response => {
        localStorage.setItem('token', JSON.stringify(response.data.token))
        localStorage.setItem('fullname', JSON.stringify(response.data.fullname))
        localStorage.setItem('email', JSON.stringify(response.data.email)) 
        alert("Login Successful")
        redirect('/dashboard')
     
      })
      .catch(error => {
        console.log(error);
      });
    }

  return (
    <div className='body'>
   
    <div className='container'>
      <div className='form-container'>
        <div className='form-toggle'>

       
          <button className={isLogin ? "active" : ""} onClick={() => setIsLogin(true)}>Sign In</button>
          <button className={!isLogin ? "active" : ""} onClick={() => setIsLogin(false)}>Sign Up</button>
        </div>
        {isLogin ? <> 
          {/* Sign in Form start */}
            <div className='form'> 
              <h1>Sign In</h1>
              <input type="emall" onChange={(e)=>setEmail(e.target.value)} placeholder="Email" />
              <input type="password" onChange={(e)=>setPassword(e.target.value)} placeholder="Password" />
              <h5>Forgot Password?</h5>
              <button type='submit' className='btn-submit' onClick={handleSubmit}>Sign In</button>
              {/* <p>Don't have an account?<a href='#' onClick={() => setIsLogin(false)}>Sign Up</a></p> */}
              
            </div>
              
          {/* Sign in Form end */}
        </>: <>
          {/* Sign up Form start */}
            <div className='form'>
              <h1>Sign Up</h1>
              <input type="emall" placeholder="Email" />
              <input type="password" placeholder="Password" />
              <input type="password" placeholder="Confirm Password" />
              <button>Sign Up</button> 
            </div>
             
          {/* Sign up Form end */}
        </> 
      }
    </div> 
  </div>   
            
    </div>
  )
 
   
}


export default LoginSignupComponent
