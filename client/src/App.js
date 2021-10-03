import logo from './logo.svg';
import './App.css';
import './CRT.css';
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
      <h1 class="crt site-title">
      r/huston-we-have-a-problem
      </h1>

        <p>
          Development build, work still in progress...
        </p>
        <a
          className="App-link"
          href="https://2021.spaceappschallenge.org/challenges/statements/lunar-surface-operations-real-time-collaboration/teams/rhuston-we-have-a-problem/project"
          target="_blank"
          rel="noopener noreferrer"
        >
        </a>
    </div>
    <div>
        <Switch>
              <Route path="/" exact={true}>
                <Login />
              </Route>
        </Switch>
    </div>
    </Router>
  );
}

export default App;