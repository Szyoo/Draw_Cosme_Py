import unittest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from app.drivers import driver_manager
from app.services.page_services.survey import Survey  # 请确保这个路径是正确的


class TestSurvey(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        driver_manager.initialize_chromedriver()
        cls.driver = driver_manager.get_driver()  # 获取 driver 实例
        cls.driver.get(
            "https://www.cosme.net/tieup/00000202309-01/page/page.html")
        # 在页面加载完毕后，暂停并等待用户输入
        input("请检查网页加载情况，输入 'ok' 后按 Enter 继续：")
        cls.survey = Survey(cls.driver)
        cls.q_blocks = cls.survey.get_q_blocks()  # 只执行一次，并存储结果

    def test_get_q_blocks(self):
        if self.q_blocks is not None:
            print("----开始执行 test_get_q_blocks 测试----")
            print(f"问题区块总数：{len(self.q_blocks)}")  # 使用存储的结果
            for i, element in enumerate(self.q_blocks):
                print(f"区块 {i + 1} - ID: {element.id}, 标签名称: {element.tag_name}")

    def test_get_q_text(self):
        if self.q_blocks is not None:
            print("----开始执行 test_get_q_text 测试----")
            first_q = self.q_blocks[0]  # 使用存储的结果
            q_text = self.survey.get_q_text(first_q)
            print(f"第一个问题的文本：{q_text}")

    def test_get_q_options(self):
        if self.q_blocks is not None:
            print("----开始执行 test_get_q_options 测试----")
            first_q = self.q_blocks[0]  # 使用存储的结果
            options = self.survey.get_q_options(first_q)
            print(f"第一个问题的选项总数：{len(options)}")
            for i, option in enumerate(options):
                print(
                    f"选项 {i + 1} - 文本: {option['text']}, 类型: {option['type']}")

    def test_get_send_btn(self):
        print("----开始执行 test_get_send_btn 测试----")
        send_btn = self.survey.get_send_btn()
        print(f"提交按钮 - ID: {send_btn.id}, 标签名称: {send_btn.tag_name}")

    def test_get_profile_fields(self):
        print("----开始执行 test_get_profile_fields 测试----")
        profile_fields = self.survey.get_profile_fields()
        print(f"个人信息字段总数：{len(profile_fields)}")
        for i, field in enumerate(profile_fields):
            print(
                f"字段 {i + 1} - ID: {field.id}, 标签名称: {field.tag_name}, 类型: {field.get_attribute('type')}")

    def test_check_already_answered(self):
        print("----开始执行 test_check_already_answered 测试----")
        is_answered = self.survey.check_already_answered()
        print(f"是否已回答：{is_answered}")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main()
