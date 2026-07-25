from pydantic import BaseModel,field_validator

class Game(BaseModel):
    id:int
    name:str
    price:float
    genre:str

