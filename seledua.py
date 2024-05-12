import unittest
from selenium import webdriver

class MoNyaPunyaBaba(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Edge()

    def test_judul(self):
        self.browser.get('http://pigg.ameba.jp')
        self.assertIn('PC版アメーバピグはサービスを終了いたしました', self.browser.title)

    def tearDown(self):
        self.browser.close()

unittest.main()