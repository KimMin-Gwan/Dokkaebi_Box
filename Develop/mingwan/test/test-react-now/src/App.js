import React, { Component } from 'react';
import axios from 'axios';

class ChatApp extends Component {
  state = {
    messages: [],
    newMessage: '',
  };

  componentDidMount() {
    // 웹소켓 연결 또는 초기 데이터 로드 등을 수행
    this.loadChatHistory();
  }

  // WAS로부터 채팅 기록을 가져오는 메서드
  loadChatHistory = () => {
    axios.get('http://0.0.0.0:8000/api/chat/history')
      .then(response => {
        const messages = response.data;
        this.setState({ messages });
      })
      .catch(error => {
        console.error('채팅 기록을 불러오는 중 에러 발생:', error);
      });
  };

  // WAS에 새 메시지를 전송하는 메서드
  sendMessage = () => {
    const { newMessage } = this.state;

    axios.post('http://0.0.0.0:8000/api/chat/send', { message: newMessage })
      .then(response => {
        // 메시지가 성공적으로 전송됨
        // 필요한 업데이트 로직을 추가
        this.setState({ newMessage: '' });
      })
      .catch(error => {
        console.error('메시지 전송 중 에러 발생:', error);
      });
  };

  render() {
    const { messages, newMessage } = this.state;

    return (
      <div>
        <div className="chat-history">
          {messages.map((message, index) => (
            <div key={index}>{message.text}</div>
          ))}
        </div>
        <div className="chat-input">
          <input
            type="text"
            value={newMessage}
            onChange={(e) => this.setState({ newMessage: e.target.value })}
          />
          <button onClick={this.sendMessage}>전송</button>
        </div>
      </div>
    );
  }
}

export default ChatApp;
