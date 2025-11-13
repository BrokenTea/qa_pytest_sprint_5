import pytest
import random
import string
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import RegistrationPageLocators, LoginPageLocators, MainPageLocators

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def generate_name():
    """Генерация имени и фамилии"""
    names = ["ivan", "maria", "alex", "olga", "dmitry", "anna", "sergey", "ekaterina", 
             "andrey", "natalia", "vladimir", "svetlana", "mikhail", "tatyana"]
    
    last_names = ["ivanov", "petrov", "sidorov", "smirnov", "kuznetsov", "popov", 
                  "vasiliev", "morozov", "volkov", "romanov", "fedorov"]
    
    name = random.choice(names)
    last_name = random.choice(last_names)
    
    return {
        'first_name': name.capitalize(),
        'last_name': last_name.capitalize(),
        'first_name_lower': name.lower(),
        'last_name_lower': last_name.lower()
    }

@pytest.fixture
def generate_email(generate_name):
    """Генерация email в формате: имя_фамилия_номер_когорты_любые_3_цифры@домен"""
    domains = ["gmail.com", "yandex.ru", "mail.ru", "hotmail.com", "outlook.com"]

    name_data = generate_name
    group_number = random.randint(1, 99)
    group_formatted = f"{group_number:02d}"
    random_digits = ''.join([str(random.randint(0, 9)) for _ in range(3)])
    
    email = f"{name_data['first_name_lower']}_{name_data['last_name_lower']}_{group_formatted}_{random_digits}@{random.choice(domains)}"
    
    return email

@pytest.fixture
def generate_password():
    """Генерация пароля (минимум 6 символов)"""
    min_length = 6
    max_length = 12
    password_length = random.randint(min_length, max_length)
    
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%^&*"
    
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]
    
    all_characters = lowercase + uppercase + digits + symbols
    for _ in range(password_length - 4):
        password.append(random.choice(all_characters))
    
    random.shuffle(password)
    
    return ''.join(password)

@pytest.fixture
def registered_user(driver, generate_name, generate_email, generate_password):
    """Фикстура для предварительной регистрации пользователя"""
    driver.get("https://stellarburgers.education-services.ru/register")
    
    name_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(RegistrationPageLocators.NAME_INPUT)
    )
    email_input = driver.find_element(*RegistrationPageLocators.EMAIL_INPUT)
    password_input = driver.find_element(*RegistrationPageLocators.PASSWORD_INPUT)

    name = generate_name
    email = generate_email
    password = generate_password

    name_input.send_keys(name)
    email_input.send_keys(email)
    password_input.send_keys(password)

    register_button = driver.find_element(*RegistrationPageLocators.REGISTER_BUTTON)
    register_button.click()

    WebDriverWait(driver, 10).until(
        EC.url_contains("login")
    )
    
    return {"email": email, "password": password, "name": name}

@pytest.fixture
def logged_in_user(driver, registered_user):
    """Фикстура для предварительного входа пользователя"""
    email = registered_user["email"]
    password = registered_user["password"]
    
    driver.get("https://stellarburgers.education-services.ru/login")
    
    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(LoginPageLocators.EMAIL_INPUT)
    )
    password_input = driver.find_element(*LoginPageLocators.PASSWORD_INPUT)
    submit_button = driver.find_element(*LoginPageLocators.LOGIN_BUTTON)

    email_input.send_keys(email)
    password_input.send_keys(password)
    submit_button.click()
    
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located(MainPageLocators.ORDER_BUTTON)
    )
    
    return {"email": email, "password": password, "name": registered_user["name"]}