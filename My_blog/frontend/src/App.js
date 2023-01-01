import './App.css';
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import MainPage from "./Components/MainPage/MainPage";
import SignupPage from './Components/SignupPage/SignupPage';
import SigninPage from './Components/SigninPage/SigninPage';

function App() {
  
  return (
    <div className="App">
      <Routes>
          <Route path="/" element={<MainPage />}/>
          <Route path="/signup" element={<SignupPage />}/>
          <Route path="/signin" element={<SigninPage />}/>
        </Routes>
    </div>
  );
}

export default App;
