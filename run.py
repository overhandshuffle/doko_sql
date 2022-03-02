from doppelkopf import app
from doppelkopf import create_game

if __name__ == "__main__":
    print(create_game.create([1,2,3,4]))
    app.run(host="127.0.0.1", debug=True)
