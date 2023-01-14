import React, { useEffect, useState } from 'react';
import Post from './Post';
import axios from 'react-axios';

function Posts (props) {

    cost [ postList, setPostList ] = useState([]);
    

    useEffect(() => {
        axios({
            url: "/user/allposts",
            headers: {
              Authorization: "Bearer " + props.token,
            },
          })
        .then((response) => {
            const data = response.data
            setPostList(data.map((post) => ({...post.data(), id: post.postID})));
        })
        .catch((error) => {
            if(error.response) {
                console.log(error.response);
            }
        })
    })

    return (
        <div>
            {postList.map((post) => {
                return (
                    <div>
                        <div>
                            <div className='title'>
                                <h1>{post.title}</h1>
                            </div>
                        </div>
                        <div className='postTextContainer'>{post.content}</div>
                        <h3>@{post.userName}</h3>
                        <h3>@{post.date}</h3>
                    </div>
                )
            })}
        </div>
    )
}

export default Posts;