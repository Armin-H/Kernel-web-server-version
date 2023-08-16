"""
    this file will make a server 
    and add different APIs from blueprints to the server
"""

from flask import Flask
from components.game import Game
import tools.read_config as read_config
import tools.check_token as check_token

debug = False

# read map file 
main_game = Game()
main_game.read_map('maps/map1.json')

# debugger for map
if debug:
    print("list of nodes: ")
    for i in range(len(main_game.list_of_nodes)):
        print([i.id for i in main_game.list_of_nodes[i].adj_main_map])
    print("end of list of nodes")

# initialize the flask app
app = Flask(__name__)
app.app_context().push()


# set the secret key
app.config['SECRET_KEY'] = 'your-secret-key'

# set the main_game instance in the flask global variable
app.config['main_game'] = main_game

# set the read_config function in the flask global variable
app.config['config'] = read_config.read_config()

# set the check_token function in the flask global variable
app.config['check_token'] = check_token


# register the blueprints

# import blueprints
from blueprints.index import index
from blueprints.get_token import login
from blueprints.initial_troops import init_troop
from blueprints.ready import ready


## a blueprint for the test server
app.register_blueprint(index)

## a blueprint for the login API(get token, player_id, public_key, port for the client)
app.register_blueprint(login)

## a blueprint for the ready API
app.register_blueprint(ready)

## a blueprint for the initial troops API
app.register_blueprint(init_troop)



if __name__ == "__main__":
    app.run(debug=True, host=app.config['config']['host'], port=app.config['config']['port'])