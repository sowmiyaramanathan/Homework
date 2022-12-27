import React from "react";
import LoginPageForm from "./LoginPageForm";
import "../../styles/styles.css";

export default function LoginPageContents() {
  return (
    <div className="mainContainer">
      <div className="welcomeText">
        <h1 className="text">Welcome to EDUPAD</h1>
        <h2 className="desc">- Earn while your learn</h2>
        <h2 className="signin">Sign in to your account</h2>
      </div>
      <LoginPageForm />
    </div>
  );
}
