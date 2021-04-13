from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def SetUp(self):
        self.browser = webdriver.Chrome(executable_path='/home/ebebe/PycharmProjects/python_tdd/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrive_it_later(self):
        #웹 사이트 확인
        self.browser.get('http://localhost:8000')

        #웹 페이지 타이들과 헤더가 To-Do를 표시하고 있음
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

    if __name__ == '__main__' :
        unittest.main(warnings='ignore')
# browser = webdriver.Chrome(executable_path='/home/ebebe/PycharmProjects/python_tdd/chromedriver')
# browser.get('http://localhost:8000')
#
# assert 'Django' in browser.title
