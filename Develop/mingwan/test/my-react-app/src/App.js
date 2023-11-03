import logo from './logo.svg';
import './App.css';
import ReactDOM from "react-dom";
import MainPage from "./ChatApp";
import React, { useState, useEffect } from "react";


/*
function App() {
  const[message, setMessage] = useState("");

  useEffect(() => {
    fetch("/api")
    .then((response) => response.json())
    .then((data) => setMessage(data.message))
  }, []);

  return (
    <div className="App">
      <h1>{message}</h1>
    </div>
  )
}
*/
function App() {
  return (
    <div>
      <MainPage /> {/* MainPage 컴포넌트를 렌더링 */}
    </div>
  );
}


export default App;
