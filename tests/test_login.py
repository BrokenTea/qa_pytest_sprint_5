import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, LoginPageLocators, RegistrationPageLocators, PasswordRecoveryLocators
from urls import URLs

class TestLogin:
    """Класс для тестирования различных способов входа в систему"""
    
    def test_login_via_main_page_button(self, driver, registered_user):
        """Тест входа по кнопке «Войти в аккаунт» на главной странице"""
        email = registered_user["email"]
        password = registered_user["password"]
        
        driver.get(URLs.MAIN)
        
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON)
        )
        login_button.click()
        
        email_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        submit_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)

        email_input.send_keys(email)
        password_input.send_keys(password)
        submit_button.click()
        
        order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        
        assert order_button.is_displayed(), "Кнопка 'Оформить заказ' не отображается после входа"

    def test_login_via_personal_account_button(self, driver, registered_user):
        """Тест входа через кнопку «Личный кабинет»"""
        email = registered_user["email"]
        password = registered_user["password"]
        
        driver.get(URLs.MAIN)
        
        personal_account_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        personal_account_button.click()
        
        email_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        submit_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)

        email_input.send_keys(email)
        password_input.send_keys(password)
        submit_button.click()
        
        order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        
        assert order_button.is_displayed(), "Кнопка 'Оформить заказ' не отображается после входа"

    def test_login_via_registration_form(self, driver, registered_user):
        """Тест входа через кнопку в форме регистрации"""
        email = registered_user["email"]
        password = registered_user["password"]
        
        driver.get(URLs.REGISTER)
        
        login_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(RegistrationPageLocators.LOGIN_LINK)
        )
        login_link.click()
        
        email_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        submit_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)

        email_input.send_keys(email)
        password_input.send_keys(password)
        submit_button.click()
        
        order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        
        assert order_button.is_displayed(), "Кнопка 'Оформить заказ' не отображается после входа"

    def test_login_via_password_recovery_form(self, driver, registered_user):
        """Тест входа через кнопку в форме восстановления пароля"""
        email = registered_user["email"]
        password = registered_user["password"]
        
        driver.get(URLs.FORGOT_PASSWORD)
        
        login_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(PasswordRecoveryLocators.LOGIN_LINK)
        )
        login_link.click()
        
        email_input = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
        )
        password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
        submit_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)

        email_input.send_keys(email)
        password_input.send_keys(password)
        submit_button.click()
        
        order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        
        assert order_button.is_displayed(), "Кнопка 'Оформить заказ' не отображается после входа"