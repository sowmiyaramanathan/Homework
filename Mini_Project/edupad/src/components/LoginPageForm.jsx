import React from "react";
import "../styles/styles.css";

export default function LoginPageForm() {
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
          <button color="black" className="button">
            Sign In
          </button>
          <nbsp></nbsp>
          <button className="button">Cancel</button>
        </div>
      </div>
    </div>
  );
}
