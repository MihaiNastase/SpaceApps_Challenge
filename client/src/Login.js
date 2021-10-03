import React, {useState} from 'react';

export default function Login() {
    const [state , setState] = useState({
        userID : "",
        password : ""
    })
    //When 'submit' clicked, send details to API
    const handleSubmitClick = (e) => {
        e.preventDefault();
        sendDetails()
    }

    //JSONify the username and password
    const sendDetails = () => {
        const information =JSON.stringify({
            "username":state.userID,
            "password":state.password
        })
        return(
            <label defaultValue={state.userID}/>

        )
    }

    return(
        //Display login Form
        <div className="">
            <form>
                <div className="form-group text-left">
                <label htmlFor="userID">UserID</label>
                <input type="string"
                       className="form-control"
                       id="userID"
                       placeholder="Enter UserID"
                       value={state.userID}
                />
                </div>

                <div className="form-group text-left">
                    <label htmlFor="password">Password</label>
                    <input type="password"
                        className="form-control"
                        id="password"
                        placeholder="Password"
                        value={state.password}
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

