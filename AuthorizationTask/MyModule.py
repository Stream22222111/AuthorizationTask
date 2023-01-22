import random

logins = []
passwords = []

# функция регистрации нового аккаунта
def register(username, password=None):
    if username in logins:
        print("Ошибка: имя пользователя уже занято.")
        return
    if not password:
        password = "".join(random.choice(".,:;!_*-+()/#¤%&0123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM") for i in range(12))
        print(f"Ваш пароль: {password}")
    else:
        if check_password(password) != [True, True, True, True]:
            print("Ошибка: Пароль должен содежать буквы нижнего и верхнего регистра, цифры и спец. символы.")
            return
    logins.append(username)
    passwords.append(password)
    print("Регистрация прошла успешно!")

# функция авторизации
def login(username, password):
    if username not in logins:
        print("Ошибка: имя пользователя не найдено.")
        return
    if password != passwords[logins.index(username)]:
        print("Ошибка: пароль неверный.")
        return
    print("Успешный вход!")

# функция проверки пароля на наличие букв нижнего и верхнего регистра, цифр и спец. символов
def check_password(password):
    has_digit = False
    has_lower = False
    has_upper = False
    has_special = False

    for char in password:
        if char.isdigit():
            has_digit = True
        elif char.islower():
            has_lower = True
        elif char.isupper():
            has_upper = True
        elif not char.isalnum():
            has_special = True

    return [has_digit, has_lower, has_upper, has_special]