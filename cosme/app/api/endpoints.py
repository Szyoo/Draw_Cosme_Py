# api.endpoints.py

from fastapi import APIRouter, WebSocket, Depends
from app.websockets.websocket_logger import logger

router = APIRouter()


@router.get("/get-chromedriver-version")
def get_chromedriver_version():
    # 逻辑代码...
    return {"version": "YOUR_CHROMEDRIVER_VERSION"}


@router.post("/start-draw/")
def start_draw():
    # 启动您的抽奖脚本的逻辑代码...
    logger.info("启动抽奖脚本")
    return {"status": "Drawing started"}


@router.post("/stop-draw/")
def stop_draw():
    # 终止您的抽奖脚本的逻辑代码...
    logger.info("终止抽奖脚本")
    return {"status": "Drawing stopped"}
