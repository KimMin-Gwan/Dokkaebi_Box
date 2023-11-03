import React, { useState } from 'react';
import './ChatInput.css';


function ChatInput() {
  const [message, setMessage] = useState('');

  const handleSendMessage = () => {
    // 메시지 전송 로직을 추가하세요.
  };

  return (
    <div className="chat-input">
      <input
        type="text"
        placeholder="메시지 입력..."
        value={message}
        onChange={(e) => setMessage(e.target.value)}
      />
      <button onClick={handleSendMessage}>보내기</button>
    </div>
  );
}

export default ChatInput;
