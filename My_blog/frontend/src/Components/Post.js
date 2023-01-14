import React from "react";

function Post(props) {
  return (
    <div>
      <div>
        <p onClick={props.clicked}>{props.post.title}</p>
      </div>
      <div>
        <p>{props.post.content.slice(0, 200) + "...."}</p>
        <div>
          <button onClick={props.clicked}>Read more</button>
        </div>
      </div>
    </div>
  );
}

export default Post;
