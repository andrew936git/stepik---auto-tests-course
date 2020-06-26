from selenium import webdriver
import time 
from selenium.webdriver.support.ui import Select


try:
	link="http://suninjuly.github.io/selects2.html"
	browser = webdriver.Chrome()
	browser.get(link)
	
	element = browser.find_element_by_id("num1")
	x = element.text
	element2 = browser.find_element_by_id("num2")
	y = element2.text
	y = int(y)
	x = int(x)
	sum = x + y
	sum = str(sum)
	select = Select(browser.find_element_by_tag_name("select"))
	select.select_by_value(sum)
	button = browser.find_element_by_class_name("btn")
	button.click()

finally:
    #успеваем скопировать код за 30 секунд
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()