from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Инициализация браузера
browser = webdriver.Chrome()

try:
    # Открываем страницу (можно использовать любую из двух)
    #browser.get("https://suninjuly.github.io/selects1.html")
    browser.get("https://suninjuly.github.io/selects2.html")

    # Находим элементы с числами
    num1_element = browser.find_element(By.ID, "num1")
    num2_element = browser.find_element(By.ID, "num2")

    # Получаем текст чисел и вычисляем сумму
    num1 = int(num1_element.text)
    num2 = int(num2_element.text)
    sum_result = str(num1 + num2)  # Преобразуем в строку для поиска в списке

    # Работаем с выпадающим списком
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum_result)  # Выбираем вариант с вычисленной суммой

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