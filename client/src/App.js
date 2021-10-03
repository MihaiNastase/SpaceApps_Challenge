
import './App.css';
import './CRT.css';
import Dashboard from './Dashboard';
import Login from './Login';
import { BrowserRouter, Route, Switch} from 'react-router-dom';
import {useState, useEffect} from 'react';

function App() {
  const [token, setToken] = useState();

  if(!token) {
    return <Login setToken={setToken} />
  }
  /*
  const[logs, setLogs] = useState([]);
  useState(() => {
    fetch('http://localhost:5000/', {
      'methods':'GET',
      headers: {
        'Content-Type':'application/json'
      }
    })
    .then(resp => resp.json())
    .then(resp => console.log(resp))
    .then(resp => setLogs(resp))
    .catch(error => console.log(error))
  },[]);
  */
  return (
    <div className="crt">
      <h1 className="site-title">Application</h1>
      <BrowserRouter>
        <Switch>
          <Route path="/dashboard">
            <Dashboard />
          </Route>
        </Switch>
      </BrowserRouter>
    </div>
  );
}

export default App;