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

    def get(self) -> list[dict]:
        """Returns all data"""
        with open('db.json') as f:
            file_data = json.load(f)
        
        return file_data['data']

    def add(self, data: AddData) -> None:
        """Add new data"""
        self._find_current_index()

        with open('db.json') as f:
            file_data = json.load(f)

        file_data['data'].append({self._current_index: data})
        self._add_into_file(new_data=file_data)

    def change(self, new_data: list[dict]) -> None:
        """Change single note using new data"""
        data = {}
        data['data'] = new_data
        self._add_into_file(data)

    def search(self, search_data: dict) -> list[dict]:
        """Search relevant data"""
        search_data = {k:v for k, v in search_data.items() if v}
        all_data = self.get()

        data = []

        for i, d in enumerate(all_data, 1):
            for k, v in search_data.items():
                if search_data[k] and d[str(i)][k].lower() == search_data[k].lower() and not all_data[i-1] in data:
                    data.append(all_data[i-1])

        return data

    def _add_into_file(self, new_data: dict) -> None:
        """Rewrite db file"""
        with open('db.json', 'w') as f:
            json.dump(new_data, f)
        
    def _find_current_index(self) -> None:
        """Find next note id; used in adding data"""
        with open('db.json') as f:
            file = json.load(f)
        self._current_index = [int(i) for i in file['data'][-1].keys()][0] + 1
