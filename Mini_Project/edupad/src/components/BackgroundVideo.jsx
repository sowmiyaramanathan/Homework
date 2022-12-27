import React from "react";
import video from '../assets/backgroundVideo1.mp4'
import '../styles/styles.css'

function BackgroundVideo() {
    return (
        <div className="video">
            <video src={video} autoPlay loop muted/>
        </div>
    )
}

export default BackgroundVideo;