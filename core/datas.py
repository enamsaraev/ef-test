import json

from dataclasses import dataclass
from typing import Any


@dataclass
class AddData:
    surname: str
    name: str
    lastname: str 
    company_name: str
    work_phone: str
    phone: str

    def __call__(self, *args: Any, **kwds: Any) -> Any:
        # self._add()
        self._add()

    def _add(self):
        data, count = self._find_next_number()
        data['3'] = {'count': count}
        with open('db.json', 'w') as f:
            json.dump(data, f)

    def _find_next_number(self) -> int:
        data = self._read_db()
        return data, len(data)

    def _read_db(self) -> dict:
        with open('db.json', 'r') as f:
            data = json.loads(f.read())

        return data