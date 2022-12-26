import React from "react";
import BackgroundVideo from "../components/BackgroundVideo";
import MainPageContents from "../components/MainPageContents";
import Mainpagenavigation from "../components/Mainpagenavigation";

function Mainpage() {
    return (
    <div>
      <BackgroundVideo />
      <Mainpagenavigation />
      <MainPageContents />
    </div>
  );
}

export default Mainpage;