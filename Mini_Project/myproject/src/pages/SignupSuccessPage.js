import React from "react-dom";
import '../styles/styles.css'

export default function SignupSuccessPage() {
  return (
    <div className="SignupSuccessPage">
      <h2 className="signin">Registration successful</h2>
      <h2 className="signin">Now log in to explore</h2>
        <button className="button">
          Log In
        </button>
    </div>
  );
}
