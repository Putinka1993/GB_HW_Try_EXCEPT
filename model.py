import controller
import os
#

class Create_user:
    def __init__(self):
        us = controller.Valid_class()
        self.user = us.result_row()

    def create_user(self):
        new_user = self.user
        surname = self.user[2]
        if os.path.exists(surname + '.txt'):
            with open(surname + '.txt', 'a') as f:
                f.write(f"<{new_user[0]}><{new_user[1]}><{new_user[2]}>"
                        f"<{new_user[3]}><{new_user[4]}><{new_user[5]}>"+ '\n')
        else:
            # Если файл не существует, создайте его
            with open(surname + '.txt', 'w') as f:
                # Запишите данные в файл
                f.write(f"<{new_user[0]}><{new_user[1]}><{new_user[2]}>"
                        f"<{new_user[3]}><{new_user[4]}><{new_user[5]}>"+ '\n')
        print()
        return f"Пользователь <{new_user[0]}><{new_user[1]}><{new_user[2]}> успешно добавлен!!"



