# app/services/page_services/survey.py

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from app.services.page_services.base import BasePage  # 引入BasePage
from app.exceptions.exceptions import ElementNotFoundException


class Survey(BasePage):
    # CSS选择器文本
    QUESTION_BLOCKS = "a ~ table:nth-of-type(2)"
    QUESTION_TEXT = "td.Q_Text01"
    OPTION_LABEL = "label"
    SEND_BUTTON = "input[type='image'][name='send']"
    PROFILE_FIELD = "table[width='640'] input[type='text'], table[width='640'] input[type='number'], table[width='640'] select"

    # XPATH选择器文本
    ALREADY_ANSWERED_TEXT = "//*[text()='すでに回答済です。']"

    def __init__(self, driver):
        super().__init__(driver)  # 调用父类的构造函数

    def get_q_blocks(self):
        return self.find_elzements(By.CSS_SELECTOR, self.QUESTION_BLOCKS, "问题的主体区块")

    def get_q_text(self, q: WebElement):
        return self.find_element(By.CSS_SELECTOR, self.QUESTION_TEXT, "问题文本", q).text.strip()

    def get_q_options(self, q: WebElement):
        label_elements = self.find_elements(
            By.CSS_SELECTOR, self.OPTION_LABEL, "问题选项合集", q)
        options = [self.get_option_detail(label) for label in label_elements]
        return options

    def get_option_detail(self, label: WebElement):
        input_element = self.find_element(
            By.CSS_SELECTOR, "input", "选项输入框", label)
        input_element_type = input_element.get_attribute("type")
        label_text = label.text.strip()
        return {
            'text': label_text,
            'input': input_element,
            'type': input_element_type
        }

    def get_send_btn(self):
        return self.find_element(By.CSS_SELECTOR, self.SEND_BUTTON, "送信按钮")

    def get_profile_fields(self):
        return self.find_elements(By.CSS_SELECTOR, self.PROFILE_FIELD, "个人信息字段")

    def check_already_answered(self):
        element = self.find_element(By.XPATH, self.ALREADY_ANSWERED_TEXT, "已回答检测")
        return element is not None

    def get_questions(self):
        questions = []
        qs = self.get_q_blocks()

        for q in qs:
            question_text = self.get_q_text(q)
            options = self.get_q_options(q)

            questions.append({
                'text': question_text,
                'options': options
            })

        return questions
