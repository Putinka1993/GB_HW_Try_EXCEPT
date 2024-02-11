from datetime import date, time
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
        valid_row = self.name.get_row()
        return valid_row.split()

    def is_valid_date(self):
        birthday = self.is_valid_row()[3].split('.')
        # print(birthday)
        # day, month, year = birthday[0], birthday[1], birthday[2]
        # print(int(day), int(month), int(year))
        try:
            year, month, day = birthday[0], birthday[1], birthday[2]
            my_date = date(int(day), int(month), int(year))
            print(my_date)
        except ValueError:
            print('Ошибка ввода')
        else:
            print(birthday)
        my_date = date(int(day), int(month), int(year))


class Start_row:
    def __init__(self):
        self.user = user.input_user_information()

    def get_row(self):
        return self.user.get_row()



