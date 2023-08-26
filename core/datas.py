import json

from dataclasses import dataclass, asdict
from typing import Any


@dataclass
class AddData:
    surname: str
    name: str
    lastname: str 
    company_name: str
    work_phone: str
    phone: str
    

    def __call__(self, *args: Any, **kwds: Any) -> dict:
        return {k: v for k, v in asdict(self).items()}