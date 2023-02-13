from datetime import datetime
from pydantic import BaseModel

class User(BaseModel):
    id: int
    name = "Deivi Gonzalez"
    signup_ts: datetime | None = None
    friends: list[int] = []
    
#Desde el exterior podrianmos recibir estos datos:
external_data = {
    'id': 1001,
    'signup_ts': '2023-02-13 16:00',
    'friends': [1002, 1003, 1004]
}

user = User(**external_data)
print(user)
print(user.id)