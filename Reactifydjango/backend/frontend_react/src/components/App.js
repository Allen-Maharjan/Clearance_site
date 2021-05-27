import axios from 'axios'
import {useEffect} from 'react'
import {render} from "react-dom"
import React from 'react'


const App = () => {
  const hook = () => {
    axios
    .get('http://127.0.0.1:8000/verified/generic/list/')
    .then(response => {
      console.log(response.data)
    })
  }

  useEffect(hook, [])
  return(<h1>Hello</h1>)
}

export default App;

const container = document.getElementById("app");
render(<App />, container);