import random
import json
from flask import Flask, Response
from User import User
from Card import CARDS
app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

first_user = User(name="test1", cards=[CARDS.get("Магазин")])
second_user = User(name="test2", cards=[CARDS.get("Сыроварня"), CARDS.get("Ферма")])
current_user_index = 0
users = [first_user, second_user]

@app.route('/')
def root():
    # result_str = "Roll: %d\nUser: %s\n" % (roll, users[pv].name)
    global current_user_index
    pv = current_user_index
    current_user_index += 1
    if current_user_index >= len(users):
        current_user_index = 0

    roll = random.randint(1, 6)
    for index, user in enumerate(users):
        user.do_move(roll, current_user_index == index)

    result_str = "%d,\n" % roll
    for index, user in enumerate(users):
        result_str += json.dumps({
            "name": user.name,
            "money": user.money,
            "turn": current_user_index == index
        }, indent=4) + ',\n'
    
    return Response(result_str, mimetype="application/json")

@app.route('/<int:number>')
def run_more_that_once(number):
    for i in range(number):
        root()
    result_str = ""
    for user in users:
        result_str += json.dumps({
            "name": user.name,
            "money": user.money,
        }, indent=4) + ',\n'
    return Response(result_str, mimetype="application/json")