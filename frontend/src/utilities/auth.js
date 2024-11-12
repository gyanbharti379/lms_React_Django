import {useAuthStore} from "../store/auth"
import axios from "./axios";
import jwt_decode from "jwt-decode";
import { Cookie } from "js-cookie";
import Swal from "sweetalert2";



export const isAuthenticated = () => {
    return useAuthStore.getState().isAuthenticated
}

export const login = async (email, password) => {   
    try{
        const  {data,status} = await axios.post('user/token/', {email, password});

        if(status === 200){
            setAuthUser(data.access, data.refresh);
            alert("Login Successful")
            return {data, error: null}

            useAuthStore.getState().login()
            const decoded = jwt_decode(data.token)
            useAuthStore.getState().setUser(decoded)
            Cookie.set('token', data.token)
        }else{
            Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: data.message,
                footer: '<a href="">Why do I have this issue?</a>'
              })
        }  



        return response.data
    }catch(error){
        data: null,
        error: error.response.data?.details || "Something went wrong",
        console.log(error)
    };

   
}

export const register = async (email, password,password2) => {
    try{
        const  {data,status} = await axios.post('user/register', {email, password,password2});

    }catch(error){
        data: null,
        error: error.response.data?.details || "Something went wrong",
        console.log(error)
    };

    const response = await axios.post('user/register', {email, password,password2})  
    return response.data
}   