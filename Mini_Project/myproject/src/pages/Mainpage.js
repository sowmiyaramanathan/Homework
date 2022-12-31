import React from "react";
import BackgroundVideo from "../components/MainPage/BackgroundVideo";
import MainPageContents from "../components/MainPage/MainPageContents";
import Mainpagenavigation from "../components/MainPage/Mainpagenavigation";

function Mainpage(props) {

  const { history } = props;

    return (
    <div>
      <BackgroundVideo />
      <Mainpagenavigation history = {history}/>
      <MainPageContents />
    </div>
  );
}

export default Mainpage;