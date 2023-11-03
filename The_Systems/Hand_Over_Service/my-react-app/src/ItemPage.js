import React, { useState, useEffect } from 'react';
import './ItemPage.css'; // Import your CSS for styling

function ItemPage() {
  const [foundFlag, setFoundFlag] = useState(false);
  const [imageData, setImageData] = useState('');
  const [time, setTime] = useState("");
  const [date, setDate] = useState("");
  const [lostPlace, setLostPlace] = useState("");
  const [lat, setLat] = useState("");
  const [lng, setLng] = useState("");
  const [classification, setClassification] = useState("");
  const [itemImage, setItemImage] = useState(null);

  useEffect(() => {
    fetch("http://127.0.0.1:8001/getImage")
      .then(response => response.json())
      .then(data => setImageData(data.image_data))
      .catch(error => console.error('이미지 데이터 가져오기 실패', error));

    fetch("http://127.0.0.1:8001/getItem")
      .then((response) => response.json())
      .then((data) => {
        setFoundFlag(data.flag);
        setTime(data.losttime);
        setDate(data.date);
        setLostPlace(data.lostPlace);
        setLat(data.let);
        setLng(data.lng);
        setClassification(data.classification);
        if (data.itemImageURL) {
          setItemImage(data.itemImageURL); // 이미지 URL을 상태 변수에 저장
        }
      });



  }, []);

  return (
    <div className="container">
      <h1> 아래의 물건이 등록됩니다. 감사합니다.</h1>
      <div className="image-container">
        {imageData && <img src={`data:image/jpeg;base64,${imageData}`} alt="이미지" />}
      </div>
      <div className="content-container">
        <h1>시간 : {time}</h1>
        <h1>날짜 : {date}</h1>
        <h1>위치명 : {lostPlace}</h1>
        <h1>경도 : {lat}</h1>
        <h1>위도 : {lng}</h1>
        <h1>종류 : {classification}</h1>
        {itemImage && (
          <img src={itemImage} alt="아이템 이미지" />
        )}
      </div>
    </div>
  );
}

export default ItemPage;


