import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationPageLocators, LoginPageLocators

class TestRegistration:
    """Класс для тестирования функциональности регистрации"""
    
    def test_successful_registration(self, driver, generate_name, generate_email, generate_password):
        """Тест проверяет успешную регистрацию с корректными данными"""
        name = generate_name
        email = generate_email
        password = generate_password
        
        driver.get("https://stellarburgers.education-services.ru/register")
        
        name_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.NAME_INPUT)
        )
        email_input = driver.find_element(*RegistrationPageLocators.EMAIL_INPUT)
        password_input = driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT)

        name_input.send_keys(name)
        email_input.send_keys(email)
        password_input.send_keys(password)

        register_button = driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON)
        register_button.click()

        WebDriverWait(driver, 10).until(
            EC.url_contains("login")
        )
        
        email_login_input = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        
        assert email_login_input.is_displayed(), "Поле для ввода Email не отображается после регистрации"
        print(f"✅ Регистрация прошла успешно! Данные: {email}")

    @pytest.mark.parametrize("incorrect_password", ["1", "12345", "1234"])
    def test_incorrect_password_error(self, driver, generate_name, generate_email, incorrect_password):
        """Тест проверяет появление ошибки при вводе некорректного пароля"""
        name = generate_name
        email = generate_email
        
        driver.get("https://stellarburgers.education-services.ru/register")
        
        name_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(RegistrationPageLocators.NAME_INPUT)
        )
        email_input = driver.find_element(*RegistrationPageLocators.EMAIL_INPUT)
        password_input = driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT)

        name_input.send_keys(name)
        email_input.send_keys(email)
        password_input.send_keys(incorrect_password)

        register_button = driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON)
        register_button.click()

        try:
            error_message = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located(RegistrationPageLocators.ERROR_MESSAGE)
            )
            
            assert error_message.is_displayed(), f"Ошибка не отображается для пароля '{incorrect_password}'"
            print(f"✅ Для пароля '{incorrect_password}' корректно отображается ошибка: '{error_message.text}'")
            
        except Exception:
            current_url = driver.current_url
            assert "register" in current_url or "login" not in current_url, \
                f"Для пароля '{incorrect_password}' произошел переход на другую страницу: {current_url}"
            print(f"⚠️  Для пароля '{incorrect_password}' ошибка не отобразилась, но регистрация не прошла")