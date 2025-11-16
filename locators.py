from selenium.webdriver.common.by import By

# Главная страница
class MainPageLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти в аккаунт')]")
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[contains(text(), 'Личный Кабинет')]")
    ORDER_BUTTON = (By.XPATH, "//button[contains(text(), 'Оформить заказ')]")
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[contains(text(), 'Конструктор')]")
    LOGO = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")
    
    # Разделы конструктора
    BUNS_SECTION = (By.XPATH, "//span[contains(text(), 'Булки')]/parent::div")
    SAUCES_SECTION = (By.XPATH, "//span[contains(text(), 'Соусы')]/parent::div")
    FILLINGS_SECTION = (By.XPATH, "//span[contains(text(), 'Начинки')]/parent::div")
    
    # Заголовки разделов конструктора (H2)
    BUNS_HEADER = (By.XPATH, "//h2[contains(text(), 'Булки')]")
    SAUCES_HEADER = (By.XPATH, "//h2[contains(text(), 'Соусы')]")
    FILLINGS_HEADER = (By.XPATH, "//h2[contains(text(), 'Начинки')]")

# Страница логина
class LoginPageLocators:
    EMAIL_INPUT = (By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[contains(text(), 'Пароль')]/following-sibling::input")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")

# Страница регистрации
class RegistrationPageLocators:
    NAME_INPUT = (By.XPATH, "//label[contains(text(), 'Имя')]/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[contains(text(), 'Email')]/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[contains(text(), 'Пароль')]/following-sibling::input")
    REGISTER_BUTTON = (By.XPATH, "//button[contains(text(), 'Зарегистрироваться')]")
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")
    ERROR_MESSAGE = (By.CLASS_NAME, "input__error")

# Страница восстановления пароля
class PasswordRecoveryLocators:
    LOGIN_LINK = (By.XPATH, "//a[contains(text(), 'Войти')]")

# Личный кабинет
class PersonalAccountLocators:
    PROFILE_LINK = (By.XPATH, "//a[contains(text(), 'Профиль')]")
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выход')]")