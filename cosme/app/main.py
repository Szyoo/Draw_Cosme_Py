# main.py

from fastapi import FastAPI
from app.api import endpoints
from app.websockets import routes as websocket_routes
from app.drivers import driver_manager

app = FastAPI()

# 包括API路由
app.include_router(endpoints.router, prefix="/api")

# 包括WebSocket路由
app.include_router(websocket_routes.router)

# 初始化chromedriver
driver_manager.initialize_chromedriver()


@app.on_event("shutdown")
def shutdown_event():
    # 关闭驱动
    driver = driver_manager.get_driver()
    driver.quit()
