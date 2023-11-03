import React, { useState } from 'react';
import ChatApp from './ChatApp';
import './App.css'; // 스타일링을 위한 CSS 파일을 import

function App() {
  const [showTitleAndButton, setShowTitleAndButton] = useState(true);

  const handleButtonClick = () => {
    setShowTitleAndButton(false);
  }

  return (
    <div className="container">
      {showTitleAndButton && (
        <div className="centered-box">
          <img src="/title_img.png" alt="Image" className="image" />
          <h1 className="title">도깨비 박스</h1>
          <h3 className="subtitle">한강공원에서 잃어버린 물건을 찾아주는 도깨비</h3>
          <button className="rounded-button" onClick={handleButtonClick}>도깨비랑 상담하기</button>
        </div>
      )}

      {showTitleAndButton ? (
        null
      ) : (
        <ChatApp />
      )}
    </div>
  );
}

export default App;


/*
function App() {
  const[message, setMessage] = useState("");

  useEffect(() => {
    fetch("/api")
    .then((response) => response.json())
    .then((data) => setMessage(data.message))
  }, []);

  return (
    <div className="App">
      <h1>{message}</h1>
    </div>
  )
}
*/