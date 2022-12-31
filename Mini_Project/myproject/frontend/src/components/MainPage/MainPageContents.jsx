import React from "react";
import { Link } from "react-router-dom";
import "../../styles/styles.css";

export default function MainPageContents() {
  return (
    <div className="mainpageWordsContainer">
      <div className="welcomeText">
        <h1 className="text">Welcome to EDUPAD</h1>
        <h2 className="desc">- Earn while your learn</h2>
      </div>
      <div className="welcomeNote">
        <p>
          A platform for students to encourage living on their while still
          studying in college
        </p>
        <p>
          With <b>eduPad</b>, you can experience how it's like to run a business
          on their own
        </p>
      </div>

      <h2 className="procedure">so, How It Works?</h2>
      <div className="steps">
        <h4 className="header">Step 1:</h4>
        <p className="content">
          -Sign up on eduPad as a seller or a buyer or why not, you can be both
        </p>
        <p className="note">
          Note: Make sure to use separate email when creating account as both
          seller and buyer
        </p>
        <h4 className="header">Step 2:</h4>
        <p className="content">
          -Login to your account and fill the basic details
        </p>
        <br />
      </div>

      <div className="userSteps">
        <div className="buyer">
          <h2
            style={{
              color: "whitesmoke",
              textAlign: "center",
              fontWeight: "bold",
            }}
          >
            For Buyers
          </h2>
          <h4 className="header">Step 3:</h4>
          <p className="content">
            -Then start exploring the products listed by your friends on eduPad
          </p>
          <h4 className="header">Step 4:</h4>
          <p className="content">-Start doing shopping</p>
        </div>

        <div className="verticalline"></div>

        <div className="seller">
          <h2
            style={{
              color: "whitesmoke",
              textAlign: "center",
              fontWeight: "bold",
            }}
          >
            For Sellers
          </h2>
          <h4 className="header">Step 3:</h4>
          <p className="content">-Wait for approval from your college admin</p>

          <h4 className="header">Step 4:</h4>
          <p className="content">
            -Start adding products you want to sell and send an approval request
            to your college admin
          </p>
          <p className="note">
            Note: The request button will be there when you are adding product
            details. Only after getting approval from the admin, you will be
            able to sell the products in eduPad
          </p>

          <h4 className="header">Step 5:</h4>
          <p className="content">
            -After getting approved <em>Start doing business</em>
            <b>
              Add more products, chat with customers, receive orders and
              payments
            </b>
          </p>
        </div>
      </div>

      <h3>Experience the new way of doing College!!</h3>
      <div className="getstartedContainer">
        <Link to = "/signup"><button className="getstarted">Get Started</button></Link>
      </div>
    </div>
  );
}
