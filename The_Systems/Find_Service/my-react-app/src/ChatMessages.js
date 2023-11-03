/*
import React, { useState, useEffect } from 'react';
import "./ChatMessages.css"

function ChatMessages() {
  const itit_txt = {text : "무엇을 잃어버렸나요?", type : 'server-message'}
  const [messages, setMessages] = useState([itit_txt]);
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
        <h1>HanGang Dokkaebi</h1>
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

*/


import React, { useState, useEffect } from 'react';
import "./ChatMessages.css"
import ItemPage from './ItemPage';

//import resetPageAndRunItemPage from 'ResetPageAndRunItemPage'

function ChatMessages() {
  const itit_txt = {text : "무엇을 잃어버렸나요?", type : 'server-message'}
  const [messages, setMessages] = useState([itit_txt]);
  const [newMessage, setNewMessage] = useState('');
  const [socket, setSocket] = useState(null);
  const [showTitleAndButton, setShowTitleAndButton] = useState(true);
  //state = { messages: [], newMessage : '' };

  useEffect(() => {
  const newSocket = new WebSocket('ws://127.0.0.1:8000/'); // 서버 주소를 적절히 변경하세요

  newSocket.onopen = () => {
    console.log('WebSocket 연결 성공');
  };

  newSocket.onmessage = (event) => {
  // 메시지가 '찾았다'인 경우 초기화하고 ItemPage 함수 실행
    if (event.data === '찾았다') {
      setShowTitleAndButton(false);
    }
    else {
      setMessages((prevMessages) => {
        const newMessages = [...prevMessages, { text : event.data, type: 'server-message' }];
        console.log(newMessages);
        return newMessages;
      });
    }
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
    <div className="container">
      {showTitleAndButton && (
        <div className="chat-messages">
            <h1>HanGang Dokkaebi</h1>
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
      )}

      {showTitleAndButton ?  (
        null
      ) : (
        <ItemPage />
      )}
    </div>
  );
}

export default ChatMessages;
