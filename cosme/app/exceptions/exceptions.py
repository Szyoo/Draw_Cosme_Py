# exceptions/exceptions.py

class ElementNotFoundException(Exception):
    """
    当在页面中未找到预期的元素时引发的异常。
    """
    def __init__(self, message):
        self.message = message

    def __str__(self):
        print(self.message)
