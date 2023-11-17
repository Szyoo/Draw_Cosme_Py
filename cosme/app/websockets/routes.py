# websockets.routes.py

from fastapi import APIRouter, WebSocket
from app.websockets import websocket_logger
from websocket_logger import logger

router = APIRouter()


@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    # 设置全局 WebSocket 连接
    websocket_logger.websocket_instance = websocket

    # 当 WebSocket 连接被接受时，发送一个消息
    logger.info("已建立连接")

    while True:
        data = await websocket.receive_text()
        # 这里可以处理从客户端接收到的其他消息
        # 例如，处理 'submitChoice' 事件
        if data == "some_message_from_client":
            # 处理客户端消息的代码...
            pass
