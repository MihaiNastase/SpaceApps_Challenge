import React, {useState} from 'react';

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
        const information =JSON.stringify({
            "username":state.username,
            "password":state.password
        })
        return(
            <label defaultValue={state.username}/>

        )
    }

    return(
        //Display login Form
        <div className="">
            <form method="post">
                <div className="form-group text-left">
                <label htmlFor="userID">UserID</label>
                <input type="string"
                       className="form-control"
                       id="userID"
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

