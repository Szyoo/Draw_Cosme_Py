# drivers.driver_manager.py

from fastapi import Depends, HTTPException
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver_instance = None


def initialize_chromedriver():
    """
    初始化并配置ChromeDriver。

    这个方法应当在您的应用启动时被调用一次，以确保在其他方法中需要时能够访问到WebDriver实例。
    """
    global driver_instance

    chrome_options = webdriver.ChromeOptions()

    # 例如，如果您想启动浏览器的无头模式：
    # chrome_options.add_argument("--headless")

    # 添加其他选项 ...
    # chrome_options.add_argument("--disable-gpu")
    # chrome_options.add_argument("--window-size=1920x1080")
    chrome_options.add_argument("--log-level=3")  # 只显示严重错误

    # 这会自动下载并缓存最新的chromedriver，无需手动管理版本
    executable_path=ChromeDriverManager().install()
    print(type(executable_path))
    print(executable_path)


    try:
        # driver_instance = webdriver.Chrome(executable_path)
        # driver_instance = webdriver.Chrome(
        #     executable_path=ChromeDriverManager().install(), options=chrome_options)
        service = Service(executable_path)
        driver_instance = webdriver.Chrome(service=service, options=chrome_options)
    except Exception as e:
        raise Exception(f"ChromeDriver初始化失败: {str(e)}")


def get_driver():
    """
    获取当前的WebDriver实例。

    如果WebDriver尚未初始化，则会引发异常。
    """
    global driver_instance

    if driver_instance:
        return driver_instance
    else:
        raise HTTPException(
            status_code=500, detail="Driver未初始化。首先调用initialize_chromedriver方法。")

# 如果您希望在FastAPI的依赖注入中使用这个driver，您可以定义一个依赖函数：


def get_driver_dependency() -> webdriver.Chrome:
    """
    FastAPI依赖注入函数，返回当前的WebDriver实例。
    """
    return get_driver()
