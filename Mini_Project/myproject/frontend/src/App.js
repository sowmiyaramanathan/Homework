import React from "react";
import LoginPage from "./pages/LoginPage.js";
import Mainpage from './pages/Mainpage.js'
import SignupPage from "./pages/SignupPage.js";
import SignupSuccessPage from "./pages/SignupSuccessPage.js";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";

function App() {
  return (
        <Routes>
          <Route path="/" element={<Mainpage />}/>
          <Route path="/signin" element={<LoginPage />} />
          <Route path="/signup" element={ <SignupPage />} />
          <Route path="/onboarding" element={ <SignupSuccessPage />} />
        </Routes>
  );
}

export default App;
