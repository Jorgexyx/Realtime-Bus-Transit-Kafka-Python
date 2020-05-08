import React from 'react';
import logo from './logo.svg';
import './App.css';

function App() {
  const source = new EventSource('/api/transit'); 
  source.onmessage = e => console.log("STREAMING")

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
