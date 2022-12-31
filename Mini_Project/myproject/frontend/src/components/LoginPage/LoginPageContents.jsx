import React, { useState } from "react";
import "../../styles/styles.css";
import axios from 'axios';

function LoginPageContents() {
  return (
    <div className="mainContainer">
      <div className="welcomeText">
        <h1 className="text">Welcome to EDUPAD</h1>
        <h2 className="desc">- Earn while your learn</h2>
        <h2 className="signin">Sign in to your account</h2>
        <LoginPageForm />
      </div>
    </div>
  );
}

function LoginPageForm() {

  const [ name, setName ] = useState([{}])

  function onClick () {
    axios({
      method: "GET",
      url: '/data'
    })
    .then((response) => {
      const res = response.data
      setName(({
        name: res.Name
      }))
      console.log(name)
    }).catch((error) => {
      if(error.response) {
        console.log(error.response)
      }
    })
  }
  return (
    <div className="formContainer">
      <div className="form-body">
        <div className="userName">
          <label className="form_label">Username</label>
          <input
            placeholder="Enter username"
            type="text"
            className="form_input"
            id="inpUserName"
          ></input>
        </div>
        <div className="userPassword">
          <label className="form_label">Password</label>
          <input
            placeholder="Enter password"
            type="text"
            className="form_input"
            id="inpUserPassword"
          ></input>
        </div>
        <div className="buttonContainer">
          <button className="button" onClick={onClick}>
            Log In
          </button>
          <nbsp></nbsp>
          <button className="button">Cancel</button>
        </div>
      </div>
    </div>
  );
}


export default LoginPageContents