import React from "react";
import "../../styles/styles.css";
import SignupPageForm from "./SignupPageForm";

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
