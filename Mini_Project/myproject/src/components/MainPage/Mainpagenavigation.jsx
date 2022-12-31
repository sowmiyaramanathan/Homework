import React from "react";
import "../../styles/styles.css";
import { Link } from "react-router-dom";

function Mainpagenavigation() {


  return (
    <div>
      <nav className="navBar">
        <ul>
          <li>
            <Link to="/signin"> <button>Sign In</button> </Link>
          </li>
          <li>
            <Link to="/signup"><button>Sign Up</button></Link>
          </li>
        </ul>
      </nav>
    </div>
  );
}

export default Mainpagenavigation;
