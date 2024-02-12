from datetime import date
import user
class Valid_class:

    def __init__(self):
        self.name = user.input_user_information()

    def string_check(self):
        try:
            if not self.name.get_row() or len(self.name.get_row().split(" ")) != 6:
                print('IS NOT VALID DATA!')
                raise Exception("Неверно указаны данные! ведите значения заново")
        except Exception as e:
            print(e)
            start = Valid_class()
            return start.string_check()
        else:
            return self.is_valid_row()

    def is_valid_row(self):
        valid_row = self.name.get_row().split()
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
            except ValueError as v:
                print(v)
                print('Ошибка ввода')
                valid_row[3] = input("Введите новую дату: ")

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

        return valid_row

    def is_valid_gender(self):
        valid_row = self.is_valid_phone()
        phone = valid_row[5].lower()
        flag = True
        while flag:
            try:
                if phone != "f" or phone != "m":
                    print('IS NOT VALID DATA!')
                    raise Exception("Неверно указаны данные! ведите значения заново")
                else:
                    flag = False
            except Exception as e:
                print(e)
                phone = input("Введите новые данные о гендере: ")
                valid_row[5] = phone

        return valid_row

class Start_row:
    def __init__(self):
        self.user = user.input_user_information()

    def get_row(self):
        return self.user.get_row()



