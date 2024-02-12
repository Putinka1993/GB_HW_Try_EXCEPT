import controller

class input_user_information:
    print("Введите данные пользователя в разделяя все данные пробелом, в формате -")
    print()
    print("Фамилия Имя Отчество датарождения номертелефона пол")
    print()
    print("Фамилия Имя Отчество датарождения(dd.mm.yyyy) номертелефона пол")

    def __init__(self):
        self.user = input("Введите свои значения: ")

    def get_row(self):
        return self.user
