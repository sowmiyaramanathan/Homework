import React from "react";
import SelectYearOfStudy from "./SelectYearOfStudy";
import "../../styles/styles.css";
import { useState } from "react";

export default function SignupPageContents() {
  return (
    <div className="mainContainer">
      <div className="welcomeText">
        <h1 className="text">Welcome to EDUPAD</h1>
        <h2 className="desc">- Earn while your learn</h2>
        <h2 className="signin">Sign up to create your account</h2>
      </div>
      <SignupPageForm />
    </div>
  );
}

function SignupPageForm() {

  const[ userName, setUserName ] = useState(null);
  const[ userEmail, setUserEmail ] = useState(null);
  const[ userPassword, setUserPassword ] = useState(null);
  const[ confirmPassword, setConfirmPassword ] = useState(null);
  const[ phoneNumber, setPhoneNumber ] = useState(null);
  const[ rollNumber, setRollNumber ] = useState(null);
  const[ regNumber, setRegNumber ] = useState(null);
  const[ yearOfStudy, setYearOfStudy ] = useState(null);
  const[ department, setDepartment ] = useState(null);
  const[ section, setSection ] = useState(null);
  
  function onHandleChange (change) {
    const {id, value} = change.target;
    if(id === "inpUserName") {
      setUserName(value)
    }
    if(id === "inpUserEmail") {
      setUserEmail(value)
    }
    if(id === "inpUserPassword") {
      setUserPassword(value)
    }
    if(id === "inpUserConfirmPassword") {
      setConfirmPassword(value)
    }
    if(id === "inpUserPhoneNumber") {
      setPhoneNumber(value)
    }
  }

  function onClickSignUp () {
    console.log(userName, userEmail, userPassword, confirmPassword, phoneNumber)
  };

  return (
    <div className="formContainer signup">
      <div className="form-body">
        <div className="field userName">
          <label className="form_label">Name</label>
          <input
            placeholder="Enter your name"
            type="text"
            className="form_input"
            id="inpUserName"
            onChange={(e) => onHandleChange(e)}
          ></input>
        </div>
        <div className="field userEmail">
          <label className="form_label">Email</label>
          <input
            placeholder="Enter your email"
            type="email"
            className="form_input"
            id="inpUserEmail"
            onChange={(e) => onHandleChange(e)}
          ></input>
        </div>
        <div className="field userPassword">
          <label className="form_label">Password</label>
          <input
            placeholder="Enter password"
            type="password"
            className="form_input"
            id="inpUserPassword"
            onChange={(e) => onHandleChange(e)}
          ></input>
        </div>
        <div className="field userConfirmPassword">
          <label className="form_label">Confirm Password</label>
          <input
            placeholder="Enter your password again"
            type="password"
            className="form_input"
            id="inpUserConfirmPassword"
            onChange={(e) => onHandleChange(e)}
          ></input>
        </div>
        <div className="field userPhoneNumber">
          <label className="form_label">Phone Number</label>
          <input
            placeholder="Enter your phone number"
            type="text"
            className="form_input"
            id="inpUserPhoneNumber"
            onChange={(e) => onHandleChange(e)}
          ></input>
        </div>
        <div className="field userRollNumber">
          <label className="form_label">Roll Number</label>
          <input
            placeholder="Enter your roll number"
            type="text"
            className="form_input"
            id="inpUserRollNumber"
            onChange={(e) => onHandleChange(e)}
          ></input>
        </div>
        <div className="field userRegNumber">
          <label className="form_label">Register Number</label>
          <input
            placeholder="Enter your register number"
            type="text"
            className="form_input"
            id="inpUserRegNumber"
            onChange={(e) => onHandleChange(e)}
          ></input>
        </div>
        <div className="field userYearOfStudy">
          <label className="form_label">Year Of Study</label>
          <SelectYearOfStudy id="inpUserYearOfStudy" />
        </div>
        <div className="field userDepartment">
          <label className="form_label">Your Department</label>
          <input
            placeholder="Enter your department"
            type="text"
            className="form_input"
            id="inpUserDepartment"
            onChange={(e) => onHandleChange(e)}
          ></input>
        </div>
        <div className="field userSection">
          <label className="form_label">Section</label>
          <input
            placeholder="Enter your section"
            type="text"
            className="form_input"
            id="inpUserSection"
            onChange={(e) => onHandleChange(e)}
          ></input>
        </div>

        <div className="buttonContainer">
          <button className="button" onSubmit={onClickSignUp()}>
            Sign Up
          </button>
          <nbsp></nbsp>
          <button className="button">Cancel</button>
        </div>
      </div>
    </div>
  );
}
