/*
import React, { useState, useEffect } from 'react';
import './ChatMessages.css'


function ChatMessages() {
  const [messages, setMessages] = useState([]);
  const [newMessage, setNewMessage] = useState('');
  const [socket, setSocket] = useState(null);

  useEffect(() => {
    const newSocket = new WebSocket('ws://127.0.0.1:8000/');

    newSocket.onopen = () => {
      console.log('WebSocket 연결 성공');
    };

    newSocket.onmessage = (event) => {
      const receivedMessage = event.data; // 메시지 파싱
      setMessages([...messages, { text: receivedMessage, type: 'server-message' }]);
    };

    setSocket(newSocket);

    return () => {
      newSocket.close();
    };
  }, [messages]);

  const handleSendMessage = () => {
    if (newMessage.trim() !== '' && socket) {
      socket.send(newMessage);
      setMessages([...messages, { text: newMessage, type: 'user-message' }]);
      setNewMessage('');
    }
  };

  return (
    <div className="chat-messages">
      <ul>
        {messages.map((message, index) => (
          <li key={index} className={`message ${message.type}`}>
            {message.text}
          </li>
        ))}
      </ul>
      <input
        type="text"
        placeholder="메시지 입력..."
        value={newMessage}
        onChange={(e) => setNewMessage(e.target.value)}
      />
      <button onClick={handleSendMessage}>보내기</button>
    </div>
  );
}

export default ChatMessages;

import React, { useState, useEffect } from 'react';
import './ChatMessages.css'

function ChatMessages() {
  const [messages, setMessages] = useState([]);
  const [newMessage, setNewMessage] = useState('');
  const [socket, setSocket] = useState(null);

  useEffect(() => {
    const newSocket = new WebSocket('ws://127.0.0.1:8000/');

    newSocket.onopen = () => {
      console.log('WebSocket 연결 성공');
    };

    newSocket.onmessage = (event) => {
      // 서버에서 받은 메시지를 클라이언트에 추가
      const messageFromServer = `서버: ${event.data}`;
      setMessages([...messages, messageFromServer]);
    };

    setSocket(newSocket);

    return () => {
      newSocket.close();
    };
  }, [messages]);

  const handleSendMessage = () => {
    if (newMessage.trim() !== '' && socket) {
      // 클라이언트에서 보낸 메시지를 서버에 전송
      socket.send(newMessage);

      // 클라이언트에서 보낸 메시지를 클라이언트에 추가
      const messageFromClient = `나: ${newMessage}`;
      setMessages([...messages, messageFromClient]);

      setNewMessage('');
    }
  };

  return (
    <div className="chat-messages">
      <ul>
        {messages.map((message, index) => (
          <li key={index}>{message}</li>
        ))}
      </ul>
      <input
        type="text"
        placeholder="메시지 입력..."
        value={newMessage}
        onChange={(e) => setNewMessage(e.target.value)}
      />
      <button onClick={handleSendMessage}>보내기</button>
    </div>
  );
}

export default ChatMessages;
*/

import React, { useState, useEffect } from 'react';
import axios from 'axios'
import "./ChatMessages.css"

function ChatMessages() {
  const [messages, setMessages] = useState([]);
  const [newMessage, setNewMessage] = useState('');
  const [socket, setSocket] = useState(null);
  //state = { messages: [], newMessage : '' };

  useEffect(() => {
  const newSocket = new WebSocket('ws://127.0.0.1:8000/'); // 서버 주소를 적절히 변경하세요

  newSocket.onopen = () => {
    console.log('WebSocket 연결 성공');
  };

  newSocket.onmessage = (event) => {
  setMessages((prevMessages) => {
    const newMessages = [...prevMessages, { text : event.data, type: 'server-message' }];
    console.log(newMessages);
    return newMessages;
  });
  };


  setSocket(newSocket);

  return () => {
    //newSocket.close();
  };
  }, []);

  const handleSendMessage = () => {

    if (newMessage.trim() !== '' && socket) {
      // 메시지를 보낼 때 메시지를 WebSocket을 통해 전송
      socket.send(newMessage);
      console.log(newMessage)
      setMessages([...messages, { text: newMessage, type: 'user-message' }]);
      setNewMessage('');
    }
  };

  return (
    <div className="chat-messages">
        <h1>Dokkaebi Box</h1>
        <div className="message-container">
          <ul>
            {messages.map((message, index) => (
              <li key={index} className={`message ${message.type}`}>
                {message.text}
              </li>
            ))}
          </ul>
        </div>
      <div className="input-container">
        <input
          type="text"
          placeholder="메시지 입력..."
          value={newMessage}
          onChange={(e) => setNewMessage(e.target.value)}
        />
        <button onClick={handleSendMessage}>보내기</button>
      </div>
    </div>
  );
}

export default ChatMessages;