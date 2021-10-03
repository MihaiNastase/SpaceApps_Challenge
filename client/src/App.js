import logo from './logo.svg';
import './App.css';
import './CRT.css';
import {useState, useEffect} from 'react';

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
    {logs.map(ulog => {
      return (
        <div key = {ulog.id}>
          <h2>{ulog.user_id}</h2>
          <p>{ulog.message_text}</p>
        </div>
      )
    })}
    </div>
  );
}

export default App;