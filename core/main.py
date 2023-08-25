import sys
import json

from core.helpers import prompt
from core.datas import AddData


class Menu:
    def __init__(self):
        self.actions = {
            '1': (self._add_data, 'Добавить запись'),
            'm': (self.ac_menu, 'Показать меню'),
            'q': (sys.exit, 'Закрыть программу'),
        }
    
    def _add_data(self):

        data = AddData(
            surname=prompt('Введите фамилию'),
            name=prompt('Введите имя'),
            lastname=prompt('Введите отчество'),
            company_name=prompt('Введите наиманование организации'),
            work_phone=prompt('Введите рабочий номер телефона'),
            phone=prompt('Введите личный нмоер телефона'),
        )()
        print(json.dumps(data.surname))

        # with open('db.json', 'a') as f:
        #     json.dump(json.dumps(data), f)
    
    def ac_menu(self):
        for num, action in self.actions.items():
            print(f'{num}. {action[1]}')

    def get_actions(self):
        return self.actions
	
    def show_usage(self):
        """Показать, как исользовать"""

        commads = ', '.join(self.actions.keys())
        print(f'\nНеизвестная команда.\nВведите одну из: {commads}')


def main():
    menu = Menu()
    menu.ac_menu()

    while True:
        cmd = input('\nВведите команду:	').strip()
        
        action_tuple = menu.get_actions().get(cmd, (menu.show_usage, ''))
        action_tuple[0]()