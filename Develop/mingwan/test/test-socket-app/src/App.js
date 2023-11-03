import React, { useState, useEffect } from 'react';
import WebSocket from 'websocket';
import './App.css'

const App = () => {
  const [message, setMessage] = useState('');
  const [chatLog, setChatLog] = useState([]);
  const socket = new WebSocket('ws://localhost:8765');

  useEffect(() => {
    socket.onopen = () => {
      console.log('Connected to the server');
    };

    socket.onmessage = (event) => {
      const receivedMessage = event.data;
      setChatLog((prevLog) => [...prevLog, receivedMessage]);
    };
  }, []);

  const handleSend = () => {
    socket.send(message);
    setMessage('');
  };

  return (
    <div>
      <div>
        {chatLog.map((message, index) => (
          <div key={index}>{message}</div>
        ))}
      </div>
      <input
        type="text"
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <button onClick={handleSend}>Send</button>
    </div>
  );
};

export default App;