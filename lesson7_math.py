import math
# webdriver это и есть набор команд для управления браузером
from selenium import webdriver


# инициализируем драйвер браузера. После этой команды вы должны увидеть новое открытое окно браузера
browser = webdriver.Chrome()

# Метод get сообщает браузеру, что нужно открыть сайт по указанной ссылке
browser.get("http://suninjuly.github.io/find_link_text")

link = browser.find_element_by_link_text(str(math.ceil(math.pow(math.pi, math.e)*10000)))
link.click()


input1 = browser.find_element_by_tag_name("input")
input1.send_keys("Max")
input2 = browser.find_element_by_name("last_name")
input2.send_keys("Daubert")
input3 = browser.find_element_by_class_name("form-control.city")
input3.send_keys("Saint-Petersburg")
input4 = browser.find_element_by_id("country")
input4.send_keys("Russia")

button = browser.find_element_by_css_selector("button")
button.click()

# успеваем скопировать код за 30 секунд
time.sleep(30)
# закрываем браузер после всех манипуляций
# driver.quit()
browser.quit()
