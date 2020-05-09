import React from 'react';
import logo from './logo.svg';
import './App.css';
var source = new EventSource('/api/transit'); //ENTER YOUR TOPICNAME HERE
source.addEventListener('message', function(e){
  console.log('Message');
}, false);



function App() {


  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Real Time Maps
        </p>
      </header>
    </div>
  );
}

export default App;
