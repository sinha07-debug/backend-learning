from pydantic import BaseModel,Field,field_validator

class Game(BaseModel):
    id:int = Field(gt=0, description="unique game id")
    name:str = Field(min_length=2)
    price:float = Field(ge=0)
    genre:str = Field(min_length=2)
    ratings:float = Field(ge=0,le=5)
