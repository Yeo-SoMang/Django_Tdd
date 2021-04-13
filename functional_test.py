import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path='/home/ebebe/PycharmProjects/python_tdd/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        #웹 사이트 확인
        self.browser.get('http://localhost:8000')

        #웹 페이지 타이들과 헤더가 To-Do를 표시하고 있음
        self.assertIn('To-Do', self.browser.title)
        header_test = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_test)

        #작업 추가
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            '작업 아이템 입력'
        )

        #텍스트 상자에 입력
        inputbox.send_keys('hello')

        #엔터를 치면 페이지가 갱신되고, 1.hello 가 추가됨
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertIn(
            any(row.text == '1.hello' for row in rows),
        )

        self.fail('finish test')

if __name__ == '__main__' :
    unittest.main(warnings='ignore')
