import React from "react";
import "../../styles/styles.css";
import '../../pages/LoginPage';

function Mainpagenavigation() {
  return (
    <div>
      <nav class="navBar">
        <ul>
          <li>
            <a href="../pages/loginPage.js">Sign In</a>
          </li>
          <li>
            <a href="../pages/loginPage.js">Sign Up</a>
          </li>
        </ul>
      </nav>
    </div>
  );
}

export default Mainpagenavigation;
