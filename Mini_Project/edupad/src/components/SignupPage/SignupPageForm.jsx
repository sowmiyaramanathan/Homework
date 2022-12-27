import React from "react";
import "../../styles/styles.css";
import SelectYearOfStudy from "./SelectYearOfStudy";

export default function SignupPageForm() {
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
          ></input>
        </div>
        <div className="field userEmail">
          <label className="form_label">Email</label>
          <input
            placeholder="Enter your email"
            type="email"
            className="form_input"
            id="inpUserEmail"
          ></input>
        </div>
        <div className="field userPassword">
          <label className="form_label">Password</label>
          <input
            placeholder="Enter password"
            type="password"
            className="form_input"
            id="inpUserPassword"
          ></input>
        </div>
        <div className="field userConfirmPassword">
          <label className="form_label">Confirm Password</label>
          <input
            placeholder="Enter your password again"
            type="password"
            className="form_input"
            id="inpUserConfirmPassword"
          ></input>
        </div>
        <div className="field userPhoneNumber">
          <label className="form_label">Phone Number</label>
          <input
            placeholder="Enter your phone number"
            type="text"
            className="form_input"
            id="inpUserPhoneNumber"
          ></input>
        </div>
        <div className="field userRollNumber">
          <label className="form_label">Roll Number</label>
          <input
            placeholder="Enter your roll number"
            type="text"
            className="form_input"
            id="inpUserRollNumber"
          ></input>
        </div>
        <div className="field userRegNumber">
          <label className="form_label">Register Number</label>
          <input
            placeholder="Enter your register number"
            type="text"
            className="form_input"
            id="inpUserRegNumber"
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
          ></input>
        </div>
        <div className="field userSection">
          <label className="form_label">Section</label>
          <input
            placeholder="Enter your section"
            type="text"
            className="form_input"
            id="inpUserSection"
          ></input>
        </div>

        <div className="buttonContainer">
          <button color="black" className="button">
            Sign Up
          </button>
          <nbsp></nbsp>
          <button className="button">Cancel</button>
        </div>
      </div>
    </div>
  );
}
