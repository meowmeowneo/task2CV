from fastapi import FastAPI, UploadFile, File
import shutil
import os


from squats import check_squats
from push_ups import check
from climber import check_climber
from bicycle import check_bicycle
from pull_ups import check_pull

app=FastAPI()

@app.post("/pushUps")
async def push_ups(id:int, competition:str, video: UploadFile = File(...)):
    try:
        with open(f"cvmedia/{video.filename}", "wb") as buffer:
            shutil.copyfileobj(video.file, buffer)

        count =  await check(video.filename)

        os.remove(f"cvmedia/{video.filename}")
        return {"result":{"id":id,"competition":competition,"count":count}}
    except Exception as e:
        return {"error": f"Произошла ошибка при загрузке файла: {str(e)}"}
    

@app.post("/squats")
async def squats(video: UploadFile = File(...)):
    try:
        with open(f"cvmedia/{video.filename}", "wb") as buffer:
            shutil.copyfileobj(video.file, buffer)

        count = await check_squats(video.filename)

        os.remove(f"cvmedia/{video.filename}")
        return count
    except Exception as e:
        return {"error": f"Произошла ошибка при загрузке файла: {str(e)}"}


@app.post("/climber")
async def climber(video: UploadFile = File(...)):
    try:
        with open(f"cvmedia/{video.filename}", "wb") as buffer:
            shutil.copyfileobj(video.file, buffer)

        count = await check_climber(video.filename)

        os.remove(f"cvmedia/{video.filename}")
        return count
    except Exception as e:
        return {"error": f"Произошла ошибка при загрузке файла: {str(e)}"}
    
@app.post("/bicycle")
async def bicycle(video: UploadFile = File(...)):
    try:
        with open(f"cvmedia/{video.filename}", "wb") as buffer:
            shutil.copyfileobj(video.file, buffer)

        count = await check_bicycle(video.filename)

        os.remove(f"cvmedia/{video.filename}")
        return count
    except Exception as e:
        return {"error": f"Произошла ошибка при загрузке файла: {str(e)}"}
    
@app.post("/pullUps")
async def pull_ups(video: UploadFile = File(...)):
    try:
        with open(f"cvmedia/{video.filename}", "wb") as buffer:
            shutil.copyfileobj(video.file, buffer)

        count = await check_pull(video.filename)

        os.remove(f"cvmedia/{video.filename}")
        return count
    except Exception as e:
        return {"error": f"Произошла ошибка при загрузке файла: {str(e)}"}