# websocket.websocket_logger.py

import asyncio
import logging
from datetime import datetime

# 全局 WebSocket 变量
websocket_instance = None


class WebSocketHandler(logging.Handler):
    def emit(self, record):
        global websocket_instance
        if websocket_instance:
            formatted_record = self.format(record)
            message = {
                "type": "new_log",
                "message": {
                    "datetime": datetime.now().strftime('%m-%d %H:%M:%S'),
                    "text": formatted_record
                }
            }
            asyncio.ensure_future(websocket_instance .send_json(message))


# 创建一个名为 'websocket' 的日志记录器，并添加 WebSocketHandler
logger = logging.getLogger('websocket')
logger.setLevel(logging.INFO)
logger.addHandler(WebSocketHandler())
