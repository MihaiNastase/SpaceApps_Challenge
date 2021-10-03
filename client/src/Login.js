import React, {useState} from 'react';
import axios from "axios";

export default function Login() {
    const [state , setState] = useState({
        username : "",
        password : ""
    })
    //When 'submit' clicked, send details to API
    const handleSubmitClick = (e) => {
        e.preventDefault();
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
                        setState(prevState => ({
                            ...prevState,
                            'logged in' : 'Logging in...'
                        }))
                        return(alert("IT FUCKING WORKKS"))
                    }

            })

    }

    return(
        //Display login Form
        <div className="">
            <form action="http://localhost:5000/login" method="post">
                <div className="form-group text-left">
                    <label htmlFor="userID">Username</label>
                    <input type="string"
                           className="form-control"
                           id="username"
                           placeholder="Enter UserID"
                           value={state.username}
                           onChange={handleChange}
                />
                </div>

                <div className="form-group text-left">
                    <label htmlFor="password">Password</label>
                    <input type="password"
                           className="form-control"
                           id="password"
                           placeholder="Password"
                           value={state.password}
                           onChange={handleChange}
                    />
                </div>

                <button
                    type="submit"
                    className="btn btn-primary"
                    onClick={handleSubmitClick}
                >
                    Login
                </button>
            </form>
        </div>
    )



}