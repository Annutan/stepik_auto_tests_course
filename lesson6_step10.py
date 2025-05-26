from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    # Открываем страницу
    link = "http://suninjuly.github.io/registration1.html"  # Можно заменить на registration2.html для проверки бага
    browser = webdriver.Chrome()
    browser.get(link)

    # Явно ждём загрузки (на всякий случай)
    time.sleep(1)

    # Заполняем обязательные поля (используем уникальные селекторы)
    first_name = browser.find_element(By.CSS_SELECTOR, ".first_block .first_class input[required]")
    first_name.send_keys("Ivan")

    last_name = browser.find_element(By.CSS_SELECTOR, ".first_block .second_class input[required]")
    last_name.send_keys("Petrov")

    email = browser.find_element(By.CSS_SELECTOR, ".first_block .third_class input[required]")
    email.send_keys("test@example.com")

    # Отправляем форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем успешность регистрации
    time.sleep(1)
    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert "Congratulations! You have successfully registered!" == welcome_text

    print("Тест пройден успешно! ✅")

except Exception as e:
    print(f"Произошла ошибка: {e}")

finally:
    time.sleep(5)
    browser.quit()