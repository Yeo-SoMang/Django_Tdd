from django.http import HttpRequest
from django.test import TestCase
from django.urls import resolve

#view에서 랜더링한 문자열을 리턴하기위한 함수
from django.template.loader import render_to_string
from .views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        expected_html = render_to_string('home.html')
        #decode를 이용해 바이트 데이터를 파이썬 유니코드 문자열로 변환함.
        #이로 인해서 바이트와 바이트를 비교하는 것이 아니라 문자열끼리 비교가 가능
        self.assertEqual(response.content.decode(), expected_html)
        # self.assertTrue(response.content.startswith(b'<html>'))
        # self.assertIn(b'<title>To-Do lists</title>', response.content)
        # self.assertTrue(response.content.strip().endswith(b'</html>'))
