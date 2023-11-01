from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# 이미지 파일을 서비스하기 위해 StaticFiles를 추가합니다.
app.mount("/images", StaticFiles(directory="C:\\Users\\antl\\Desktop\\IOT한강"), name="images")

@app.get('/')
async def return_img():
    # 이미지 파일을 응답으로 반환합니다.
    # 이미지 파일은 'images' 디렉토리에 있어야 합니다.
    return FileResponse("C:\\Users\\antl\\Desktop\\IOT한강\\3.연결실패.png", media_type="image/jpeg")
 
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)