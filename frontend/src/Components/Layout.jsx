import React from 'react'
import BeforeLoginHeader from './Header/Before_Login_Header'
import Footer from './Footer/Footer_page'
import {Outlet } from 'react-router-dom'
import AfterLoginHeader from './Header/After_Login_Header'

const Layout = () => {
  const isLoggedIn = localStorage.getItem('token') !== null;
  return (
   
    <div>
        {isLoggedIn ? <AfterLoginHeader /> : <BeforeLoginHeader />}

        <Outlet />
        <Footer />

    </div>
  )
}

export default Layout