import React from "react";
import BackgroundVideo from "../components/MainPage/BackgroundVideo";
import MainPageContents from "../components/MainPage/MainPageContents";
import Mainpagenavigation from "../components/MainPage/Mainpagenavigation";

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