import MyModule

while True:
    choice = input("Выберите операцию: (r)регистрация, (l)авторизоваться, (q)выйти ").lower()
    if choice == "r":
        username = input("Введите имя пользователя: ")
        password = input("Введите пароль (или нажмите enter для создания случайного пароля): ")
        MyModule.register(username, password)
    elif choice == "l":
        username = input("Введите имя пользователя: ")
        password = input("Введите пароль: ")
        MyModule.login(username, password)
    elif choice == "q":
        break
    else:
        print("Неверная операция.")
