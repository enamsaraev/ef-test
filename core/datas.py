import json

from dataclasses import dataclass, asdict
from typing import Any

from core.helpers import prompt


@dataclass
class AddData:
    """Saves data of a single note, returns its dict"""
    surname: str
    name: str
    lastname: str 
    company_name: str
    work_phone: str
    phone: str
    

    def __call__(self, *args: Any, **kwds: Any) -> dict:
        return {k: v for k, v in asdict(self).items()}
    

@dataclass
class ChangeData:
    """Saves what data should be changed; only single note"""
    data: dict

    def __call__(self, *args: Any, **kwds: Any) -> dict:
        return self._input()

    def _input(self) -> dict:
        new_data = {}

        new_data['surname'] = prompt('Введите фамилию', default=self.data.get('surname', ''))
        new_data['name'] = prompt('Введите имя', default=self.data.get('name', ''))
        new_data['lastname'] = prompt('Введите отчество', default=self.data.get('lastname', ''))
        new_data['company_name'] = prompt('Введите наиманование организации', default=self.data.get('company_name', ''))
        new_data['work_phone'] = prompt('Введите рабочий номер телефона', default=self.data.get('work_phone', ''))
        new_data['phone'] = prompt('Введите личный нмоер телефона', default=self.data.get('phone', ''))

        return new_data
    

@dataclass
class SearchData:
    """Saves search data"""
    def __call__(self, *args: Any, **kwds: Any) -> dict:
        return self._search_data()

    def _search_data(self) -> dict:
        new_data = {}

        new_data['surname'] = prompt('Введите фамилию')
        new_data['name'] = prompt('Введите имя')
        new_data['lastname'] = prompt('Введите отчество')
        new_data['company_name'] = prompt('Введите наиманование организации')
        new_data['work_phone'] = prompt('Введите рабочий номер телефона')
        new_data['phone'] = prompt('Введите личный нмоер телефона')

        return new_data