import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


# Инициализация браузера
browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/redirect_accept.html")

try:
    # 1. Нажимаем на кнопку, которая открывает новую вкладку
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # 2. Переключаемся на новую вкладку
    browser.switch_to.window(browser.window_handles[1])

    # 3. Решаем капчу на новой странице
    # Ждем загрузки элементов на новой вкладке
    x_element = WebDriverWait(browser, 10).until(
        EC.presence_of_element_located((By.ID, "input_value"))
    )
    x = x_element.text
    y = calc(x)

    # Вводим ответ в текстовое поле
    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(y)

    # Нажимаем кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

    # 4. Получаем результат из alert
    WebDriverWait(browser, 10).until(EC.alert_is_present())
    alert = browser.switch_to.alert
    alert_text = alert.text
    print("Результат:", alert_text.split()[-1])
    alert.accept()

finally:
    # Закрываем все вкладки и браузер
    browser.quit()