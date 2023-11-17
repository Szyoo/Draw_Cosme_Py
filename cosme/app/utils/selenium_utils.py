# ultis/selenium_utils.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    NoSuchElementException, TimeoutException, NoAlertPresentException, NoSuchWindowException)
from selenium.webdriver.remote.webelement import WebElement

from app.drivers import driver_manager


def switch_to_next_window():
    """
    切换到下一个浏览器窗口。

    使用案例：
    selenium_utils.switch_to_next_window()
    """
    driver = driver_manager.get_driver()
    windows = driver.window_handles
    if len(windows) > 1:
        try:
            driver.switch_to.window(windows[1])
        except NoSuchWindowException:
            print("无法切换到下一个窗口。")


def close_all_other_windows():
    """
    关闭除当前窗口外的所有其他窗口。

    使用案例：
    selenium_utils.close_all_other_windows()
    """
    driver = driver_manager.get_driver()
    main_window = driver.current_window_handle
    for window in driver.window_handles:
        if window != main_window:
            try:
                driver.switch_to.window(window)
                driver.close()
            except NoSuchWindowException:
                print(f"无法关闭窗口: {window}")
    try:
        driver.switch_to.window(main_window)
    except NoSuchWindowException:
        print("无法返回主窗口。")


def find(by: By, value: str, timeout=10):
    """
    等待并查找一个元素。如果在超时时间内找到元素则返回该元素。

    参数:
    - by: 元素的查找方式 (例如: By.ID, By.CLASS_NAME)
    - value: 要查找元素的值 (例如: 元素的 ID, 类名)
    - timeout: 等待元素出现的最大秒数，默认为10秒
    """
    driver = driver_manager.get_driver()
    element_present = EC.presence_of_element_located((by, value))
    return WebDriverWait(driver, timeout).until(element_present)


def find_elements(by: By, value: str, timeout=10):
    """
    等待并查找多个元素。如果在超时时间内找到元素则返回这些元素的列表。

    参数:
    - by: 元素的查找方式 (例如: By.ID, By.CLASS_NAME)
    - value: 要查找元素的值 (例如: 元素的 ID, 类名)
    - timeout: 等待元素出现的最大秒数，默认为10秒
    """
    driver = driver_manager.get_driver()
    elements_presents = EC.presence_of_all_elements_located((by, value))
    return WebDriverWait(driver, timeout).until(elements_presents)


def find_child_element(parent_element: WebElement, by: By, selector: str):
    """
    在给定的父元素上查找子元素。

    使用案例：
    child_element = find_child_element(parent_element, By.CSS_SELECTOR, ".child_class", "描述")
    """
    return parent_element.find_element(by, selector)
