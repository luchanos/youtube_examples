from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel, ValidationError


class User(BaseModel):
    id: int
    name = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: List[int] = []


external_data = {
    'id': '123',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3'],
}

external_data_2 = {
    'id': '123',
    'signup_ts': '2019-06-01 12:22',
    'friends': [1, 2, '3a'],
    'some_field': 'kek'
}

try:
    user = User(**external_data_2)
except ValidationError as err:
    print(err.json())
# print(user)
