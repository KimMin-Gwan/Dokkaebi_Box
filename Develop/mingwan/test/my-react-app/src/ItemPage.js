import React, { useState, useEffect } from 'react';
import './ItemPage.css'; // 스타일링을 위한 CSS 파일을 import

function ItemPage() {
  const [foundFlag, setFoundFlag] = useState(false);
  const [time, setTime] = useState("");
  const [date, setDate] = useState("");
  const [lostPlace, setLostPlace] = useState("");
  const [lat, setLat] = useState("");
  const [lng, setLng] = useState("");
  const [classification, setClassification] = useState("");
  const [itemImage, setItemImage] = useState(null); // 이미지 URL을 저장할 상태 변수 추가

  useEffect(() => {
    fetch("http://127.0.0.1:8000/getItem")
      .then((response) => response.json())
      .then((data) => {
        setFoundFlag(data.flag);
        setTime(data.time);
        setDate(data.date);
        setLostPlace(data.lostPlace);
        setLat(data.lat);
        setLng(data.lng);
        setClassification(data.classification);
        if (data.itemImageURL) {
          setItemImage(data.itemImageURL); // 이미지 URL을 상태 변수에 저장
        }
      });
  }, []);

  return (
    <div className="container">
      {foundFlag && (
        <div className="App">
          <h1>시간 : {time}</h1>
          <h1>날짜 : {date}</h1>
          <h1>위치명 : {lostPlace}</h1>
          <h1>경도 : {lat}</h1>
          <h1>위도 : {lng}</h1>
          <h1>종류 : {classification}</h1>
          {itemImage && (
            <img src={itemImage} alt="아이템 이미지" />
          )}
          <button className="rounded-button" onClick={handleButtonClick}>내 물건이 맞아요</button>
        </div>
      )}

      {!foundFlag && <h1>찾을 수 없어요</h1>}
    </div>
  );
}

export default ItemPage;

