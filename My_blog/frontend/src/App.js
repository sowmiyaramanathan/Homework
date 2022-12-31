import logo from './logo.svg';
import './App.css';
import { useState, useEffect } from 'react'
import axios from 'axios';

function App() {

  const [ data, setData ] = useState([{}])

  useEffect(() => {
    axios({
      method: "GET",
      url: "/data"
    })
    .then((response) => {
      const res = response.data
      setData(({
        data: res.Name
      }))
      console.log(data.data)
    }).catch((error) => {
      if(error.response) {
        console.log(error.response)
      }
    })
  }, [])

  const [ name, setName ] = useState([{}])

  function onClick () {
    axios({
      method: "GET",
      url: '/data'
    })
    .then((response) => {
      const res = response.data
      setName(({
        name: res.Name
      }))
      console.log(name)
    }).catch((error) => {
      if(error.response) {
        console.log(error.response)
      }
    })
  }
  
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
        <button onClick={onClick}>Click here</button>
        <p>{name.name}</p>
      </header>
    </div>
  );
}

export default App;
