from selenium import webdriver
driver = webdriver.Chrome("/Users/hasangurbuz/Downloads/chromedriver")
#Öncelikle açılan Firefox üzerinde ‘gurayyildirim.com.tr’ adresini açalım:
driver.get("http://www.gurayyildirim.com.tr")
print (driver.title)
'Blog' in driver.title
#assert 'Blog' in driver.title

#Kaynak:https://www.gurayyildirim.com.tr/python-ve-selenium-denemeleri-1246.html
arama_butonu = driver.find_element_by_id('search-toggle')
arama_butonu.click()

arama_kutusu = driver.find_element_by_class_name('search-field')
arama_kutusu.send_keys('Kivy')
#-------------------------------------------------------------

from selenium.webdriver.common.keys import Keys
arama_kutusu.send_keys(Keys.RETURN)


print(driver.fullscreen_window())
print(driver.page_source)

driver.quit()