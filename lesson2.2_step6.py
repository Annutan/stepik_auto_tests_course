import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


# Инициализация браузера
browser = webdriver.Chrome()
browser.get("https://SunInJuly.github.io/execute_script.html")

try:
    # Считываем значение x
    x_element = browser.find_element(By.ID, "input_value")
    x = x_element.text
    y = calc(x)

    # Скроллим страницу вниз, чтобы элементы стали видимыми
    input_field = browser.find_element(By.ID, "answer")
    browser.execute_script("arguments[0].scrollIntoView(true);", input_field)

    # Вводим ответ в текстовое поле
    input_field.send_keys(y)

    # Отмечаем checkbox "I'm the robot"
    checkbox = browser.find_element(By.ID, "robotCheckbox")
    checkbox.click()

    # Выбираем radiobutton "Robots rule!"
    radiobutton = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("arguments[0].click();", radiobutton)

    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    # Ждем результат и копируем число из алерта
    WebDriverWait(browser, 10).until(EC.alert_is_present())
    alert = browser.switch_to.alert
    alert_text = alert.text
    print("Результат:", alert_text.split()[-1])
    alert.accept()

finally:
    # Закрываем браузер
    browser.quit()