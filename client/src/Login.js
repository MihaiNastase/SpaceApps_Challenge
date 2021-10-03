import React from 'react';
import './CRT.css'

export default function Login() {
  return(
    <div className="login-wrapper">
   <form>
      <label class="crt site-title">
        <p>Username</p>
        <input type="text" />
      </label>
      <label class="crt site-title">
        <p>Access key</p>
        <input type="password" />
      </label>
      <div>
        <button type="submit">Access</button>
      </div>
    </form>
    </div>
  );
}