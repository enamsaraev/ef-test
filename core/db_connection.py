import json

from dataclasses import asdict

from core.datas import AddData

{
    "settings": {},
    "data": [{"1": "test"}]
}


class DB:
    def __init__(self) -> None:
        self._current_index = 0

    def get(self):
        with open('db.json') as f:
            file_data = json.load(f)
        
        return file_data['data']

    def add(self, data: AddData):
        self._find_current_index()

        with open('db.json') as f:
            file_data = json.load(f)

        file_data['data'].append({self._current_index: data})
        self._add_into_file(new_data=file_data)

    def change(self, new_data: list[dict]):
        data = {}
        data['data'] = new_data
        self._add_into_file(data)

    def _add_into_file(self, new_data):
        with open('db.json', 'w') as f:
            json.dump(new_data, f)
        
    def _find_current_index(self) -> None:
        with open('db.json') as f:
            file = json.load(f)
        self._current_index = [int(i) for i in file['data'][-1].keys()][0] + 1
