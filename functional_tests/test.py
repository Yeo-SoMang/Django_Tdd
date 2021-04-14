import unittest

from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class NewVisitorTest(LiveServerTestCase):
    def setUp(self):
        self.browser = webdriver.Chrome(executable_path='/home/ebebe/PycharmProjects/python_tdd/chromedriver')
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows])

    def test_can_start_a_list_and_retrieve_it_later(self):
        #웹 사이트 확인
        self.browser.get(self.live_server_url)

        #웹 페이지 타이들과 헤더가 To-Do를 표시하고 있음
        self.assertIn('To-Do', self.browser.title)
        header_test = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_test)

        #작업 추가
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        #텍스트 상자에 입력
        inputbox.send_keys('hello')
        #엔터를 치면 페이지가 갱신되고, 1.hello 가 추가됨
        inputbox.send_keys(Keys.ENTER)
        # time.sleep(2)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        # self.assertTrue(
        #     any(row.text == '1: hello' for row in rows),
        #     "신규 작업이 테이블에 표시되지 않는다. -- 해당 텍스트: \n%s" % (
        #         table.text,
        #     )
        # )
        #어설션을 덜 똑똑하도록 만듦. 위의 여섯줄을 아래의 한줄로 바꿈.
        self.assertIn('1: hello', [row.text for row in rows])

        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('TDD in Django')
        inputbox.send_keys(Keys.ENTER)

        time.sleep(2)
        #page refreash
        self.check_for_row_in_list_table('2: TDD in Django')
        self.check_for_row_in_list_table('1: hello')
        # table = self.browser.find_element_by_id('id_list_table')
        # rows = table.find_elements_by_tag_name('tr')
        # self.assertIn('1: hello', [row.text for row in rows])
        # self.assertIn(
        #     '2: TDD in Django',
        #     [row.text for row in rows]
        # )

        self.fail('finish test')
