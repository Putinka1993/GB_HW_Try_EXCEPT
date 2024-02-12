from datetime import date
import user
class Valid_class:

    def __init__(self):
        self.name = user.input_user_information()

    def string_check(self):
        valid_row = self.name.get_row().split()
        while True:
            try:
                if len(valid_row) == 0 or len(valid_row) != 6:
                    print('IS NOT VALID DATA!')
                    raise Exception("Неверно указаны данные! ведите значения заново")
                else:
                    print("в общей строке валидное количество значений")
                    print()
                    return valid_row
            except Exception as e:
                print(f'Ошибка: {e}')
                valid_row = input("Введите данные заного: ").split()



    def is_valid_row(self):
        valid_row = self.string_check()
        return valid_row

    def is_valid_date(self):
        valid_row = self.is_valid_row()
        while True:
            try:
                birthday = valid_row[3].split('.')
                year, month, day = birthday[0], birthday[1], birthday[2]
                my_date = date(int(day), int(month), int(year))
                valid_row[3] = my_date.strftime('%d.%m.%Y')
                break
            except Exception as v:
                print(v)
                print('Ошибка ввода')
                valid_row[3] = input("Введите новую дату: ")
        print("в строке датарождения валидная дата")
        print()
        return valid_row

    def is_valid_phone(self):
        valid_row = self.is_valid_date()
        while True:
            try:
                valid_row[4] = int(valid_row[4])
                break
            except ValueError as v:
                print(v)
                print('Ошибка ввода телефонного номера')
                valid_row[4] = input("Введите заново телефонный номер: ")
        print("в строке телефонный номер валидный номер")
        print()
        return valid_row

    def is_valid_gender(self):
        valid_row = self.is_valid_phone()
        gender = valid_row[5].lower()
        while True:
            try:
                if gender == "m" or gender == "f":

                    valid_row[5] = gender
                    print("в строке гендер верно указан пол человека")
                    print()
                    return valid_row
                else:
                    raise Exception
            except Exception as e:
                print(f'Ошибка: {e}')
                gender = input('Введите строку еще раз: ')
    def result_row(self):
        result = self.is_valid_gender()
        return result

class Start_row:
    def __init__(self):
        self.user = user.input_user_information()

    def get_row(self):
        return self.user.get_row()



