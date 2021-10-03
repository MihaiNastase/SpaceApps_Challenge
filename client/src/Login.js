import React, {useState} from 'react';
import axios from "axios";
import './CRT.css'

export default function Login() {
        const [state , setState] = useState({
            username : "",
            password : ""
        })
        //When 'submit' clicked, send details to API
        const handleSubmitClick = (e) => {
            e.preventDefault();
            console.log(state.password)
            sendDetails()
        }
        //Handle inputs into input fields
        const handleChange = (e) => {
            const {id , value} = e.target
            setState(prevState => ({
                ...prevState,
                [id] : value
            }))
        }
        //JSONify the username and password
        const sendDetails = () => {
    
            const body = {
                "username":state.username,
                "password":state.password,
            }
    
            axios.post('http://localhost:5000/login', body)
                .then((response)=>{
                     if(response.status === 200){
                            if(response.data.status) {
                                return(alert("Access Granted!"));
                            }
                            else {
                                return(alert("Permission Denied!"));
                            }
                }
                
            })
        }

    return(
    <div className="crt login-wrapper">
    <form>
        <label class="site-title" htmlFor="userId">
            <p>Username</p>
            <input type="string" 
                id="username"
                value={state.username}
                onChange={handleChange}
            />
        </label>
        <label class="site-title">
            <p>Access key</p>
            <input type="password"
            value={state.password}               
            onChange={handleChange}
       />
        </label>
        <div>
            <button class="site-title" type="submit" onClick={handleSubmitClick}>Access</button>
        </div>
        </form>
        </div>
    
  )
}