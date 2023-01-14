import React, { useState } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import Posts from "./Posts";

function HomePage(props) {
  function signOut() {
    axios({
      url: "/user/signout",
      headers: {
        Authorization: "Bearer " + props.token,
      },
    })
      .then((response) => {
        props.removetoken();
      })
      .catch((error) => {
        if (error.response) {
          console.log(error.response);
        }
      });
  }

  

  return (
    <div>
      <h1>Welcome to your blog site</h1>

      <nav>
        <button onClick={signOut}>Sign out</button>
      </nav>

      <Link to='/user/createBlogPost'><button>Create a new blog post</button></Link>

      <div>
        <Posts token={props.token} />
      </div>
    </div>
  );
}

export default HomePage;
