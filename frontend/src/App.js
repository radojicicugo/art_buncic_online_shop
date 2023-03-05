import React, {useState} from 'react';
import './App.css';
import axios from 'axios';
import {BrowserRouter as Router, Route, Switch, useHistory  } from 'react-router-dom'
import NavBar from './components/NavBar';
import Amazon from './components/Amazon';





function App(props) {

 

  return (

<div>
  <NavBar />
  <Amazon />
</div>
  );
}

export default App;
