import logo from './logo.svg';
import './App.css';
import Login from './Login.js';
import {useState, useEffect} from 'react';
import {
  BrowserRouter as Router,
  Switch,
  Route
} from "react-router-dom";

function App() {

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

  return (
      <Router>
        <div className="App">

              <header className="App-header">
                <img src={logo} className="App-logo" alt="logo" />
                <p>
                  Development build, work still in progress...
                </p>
                <a
                  className="App-link"
                  href="https://2021.spaceappschallenge.org/challenges/statements/lunar-surface-operations-real-time-collaboration/teams/rhuston-we-have-a-problem/project"
                  target="_blank"
                  rel="noopener noreferrer"
                >
                  r/huston-we-have-a-problem
                </a>
              </header>
              <div>
                  <Switch>
                        <Route path="/" exact={true}>
                          <Login />
                        </Route>
                  </Switch>
              </div>
        </div>
      </Router>

  );
}

export default App;
