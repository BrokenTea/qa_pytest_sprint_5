import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import MainPageLocators, PersonalAccountLocators, LoginPageLocators

class TestTransition:
    """Класс для тестирования личного кабинета, конструктора и выхода из системы"""
    
    def test_navigate_to_personal_account(self, driver, logged_in_user):
        """Проверка перехода в личный кабинет по клику на «Личный кабинет»"""
        personal_account_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        personal_account_link.click()
        
        profile_text = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(PersonalAccountLocators.PROFILE_LINK)
        )
        
        assert profile_text.is_displayed(), "Не удалось перейти в личный кабинет"
        print("✅ Успешный переход в личный кабинет")

    def test_navigate_from_account_to_constructor_via_constructor(self, driver, logged_in_user):
        """Проверка перехода из личного кабинета в конструктор по клику на «Конструктор»"""
        personal_account_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        personal_account_link.click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(PersonalAccountLocators.PROFILE_LINK)
        )
        
        constructor_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)
        )
        constructor_link.click()
        
        order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        
        assert order_button.is_displayed(), "Не удалось вернуться в конструктор через ссылку 'Конструктор'"
        print("✅ Успешный переход из личного кабинета в конструктор через 'Конструктор'")

    def test_navigate_from_account_to_constructor_via_logo(self, driver, logged_in_user):
        """Проверка перехода из личного кабинета в конструктор по клику на логотип Stellar Burgers"""
        personal_account_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        personal_account_link.click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(PersonalAccountLocators.PROFILE_LINK)
        )
        
        logo = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.LOGO)
        )
        logo.click()
        
        order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        
        assert order_button.is_displayed(), "Не удалось вернуться в конструктор через логотип"
        print("✅ Успешный переход из личного кабинета в конструктор через логотип")

    def test_logout_from_account(self, driver, logged_in_user):
        """Проверка выхода из аккаунта по кнопке «Выйти» в личном кабинете"""
        personal_account_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.PERSONAL_ACCOUNT_BUTTON)
        )
        personal_account_link.click()
        
        WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(PersonalAccountLocators.PROFILE_LINK)
        )
        
        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(PersonalAccountLocators.LOGOUT_BUTTON)
        )
        logout_button.click()
        
        login_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON)
        )
        
        assert login_button.is_displayed(), "Не удалось выйти из аккаунта"
        print("✅ Успешный выход из аккаунта")
        
class TestConstructorSections:
    """Класс для тестирования разделов конструктора"""
    
    def test_constructor_buns_section(self, driver, logged_in_user):
        """Проверка перехода к разделу «Булки»"""
        order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        
        def check_active_section(expected_section):
            active_section = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, f"//div[contains(@class, 'tab_tab__1SPyG') and contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='{expected_section}']"))
            )
            return active_section.is_displayed()
        
        sauces_section = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.SAUCES_SECTION)
        )
        sauces_section.click()
        
        assert check_active_section("Соусы"), "Раздел 'Соусы' не стал активным"
        print("✅ Раздел 'Соусы' активен")
        
        buns_section = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.BUNS_SECTION)
        )
        buns_section.click()
        
        assert check_active_section("Булки"), "Раздел 'Булки' не стал активным"
        print("✅ Успешный переход к разделу 'Булки'")

    def test_constructor_sauces_section(self, driver, logged_in_user):
        """Проверка перехода к разделу «Соусы»"""
        order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        
        def check_active_section(expected_section):
            active_section = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, f"//div[contains(@class, 'tab_tab__1SPyG') and contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='{expected_section}']"))
            )
            return active_section.is_displayed()
        
        sauces_section = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.SAUCES_SECTION)
        )
        sauces_section.click()
        
        assert check_active_section("Соусы"), "Раздел 'Соусы' не стал активным"
        print("✅ Успешный переход к разделу 'Соусы'")

    def test_constructor_fillings_section(self, driver, logged_in_user):
        """Проверка перехода к разделу «Начинки»"""
        order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
        )
        
        def check_active_section(expected_section):
            active_section = WebDriverWait(driver, 5).until(
                EC.visibility_of_element_located((By.XPATH, f"//div[contains(@class, 'tab_tab__1SPyG') and contains(@class, 'tab_tab_type_current__2BEPc')]//span[text()='{expected_section}']"))
            )
            return active_section.is_displayed()
        
        fillings_section = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(MainPageLocators.FILLINGS_SECTION)
        )
        fillings_section.click()
        
        assert check_active_section("Начинки"), "Раздел 'Начинки' не стал активным"
        print("✅ Успешный переход к разделу 'Начинки'")