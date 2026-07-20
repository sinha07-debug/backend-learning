from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def home():
    return{"message":"Welcome to Video Games API"}

@app.get("/games")
def get_games():
    return {
        "games":[
        "BGMI",
        "GTA"
        ]
    }

@app.get("/games/{game_id}")
def get_game(game_id:int):
    return {"game_id":game_id}
