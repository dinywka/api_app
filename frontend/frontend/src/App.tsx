import React from 'react';
import logo from './logo.svg';
import { Counter } from './features/counter/Counter';
import './App.css';
import axios from "axios";

function App() {
  async function getData() {

  const url = "http://127.0.0.1:8000/api/";
  const response = await axios.get(url);
  console.log(response);
  }
  return (
    <div className="App">
      <header className="App-header">
        <button className={""} onClick={getData}>Get Data</button>
      </header>
    </div>
  );
}

export default App;
