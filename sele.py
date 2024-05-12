from selenium import webdriver

browser = webdriver.Edge()

browser.get('http://pigg.ameba.jp')
assert 'PC版アメーバピグはサービスを終了いたしました' in browser.title

print('Judulnya bener gan')

browser.quit()