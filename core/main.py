import sys
import json

from core.helpers import prompt, print_table
from core.datas import AddData
from core.db_connection import DB


class Menu:
    def __init__(self):
        self.db = DB()
        self.actions = {
            '1': (self._get_data, 'Смотреть записи'),
            '2': (self._add_data, 'Добавить запись'),
            'm': (self.ac_menu, 'Показать меню'),
            'q': (sys.exit, 'Закрыть программу'),
        }

    def _get_data(self):
        data = self.db.get()
        
        action, begin, end = '', 0, 3
        while action.lower() != 'q':
            print_table(
                {
                    "surname": "Фамилия", 
                    "name": "Имя", 
                    "lastname": "Отчетсво", 
                    "company_name": "Имя компании", 
                    "work_phone": "Рабочий телефон", 
                    "phone": "Личный телефон"
                },
                data[begin:end]
            )
            action = prompt('Вперед - n, назад - p, выйти - q')
            
            if action.lower() == 'n':
                begin = end
                end += 3
            elif action.lower() == 'p':
                end = begin
                begin -= 3

            if end > len(data)+1 or begin < 0:
                begin = 0
                end = 3

    def _add_data(self):
        data = AddData(
            surname=prompt('Введите фамилию'),
            name=prompt('Введите имя'),
            lastname=prompt('Введите отчество'),
            company_name=prompt('Введите наиманование организации'),
            work_phone=prompt('Введите рабочий номер телефона'),
            phone=prompt('Введите личный нмоер телефона'),
        )()
        self.db.add(data=data)
    
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