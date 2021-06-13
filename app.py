import json
import random
from flask import Flask, Response
from flask_cors import CORS
from User import User
from CARDS import CARDS
from Utils import sort

# from Utils import get_key

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
CORS(app)

first_user = User(name="test1", cards=[CARDS.get("B1"), CARDS.get("B2")],
                  attractions=[CARDS.get("O1"), CARDS.get("O3"), CARDS.get("O4"), CARDS.get("O5"), CARDS.get("O6"), CARDS.get("O7"), CARDS.get("O8"), CARDS.get("O9")], uid=1)
second_user = User(name="test2", cards=[CARDS.get("B3"), CARDS.get("B4")],
                   attractions=[CARDS.get("O1"), CARDS.get("O1")], uid=2)
third_user = User(name="test3", cards=[CARDS.get("B5"), CARDS.get("B9")], attractions=[CARDS.get("O1")], uid=3)
fourth_user = User(name="test4", cards=[CARDS.get("B7"), CARDS.get("B8")],
                   attractions=[CARDS.get("O1"), CARDS.get("O2"), CARDS.get("O5")], uid=4)
current_user_index = 0
last_roll = None
users = [first_user, second_user, third_user, fourth_user]


def make_response():
    global current_user_index
    global last_roll
    result = {'roll': last_roll, 'users': []}
    for index, user in enumerate(users):
        user_result = user.to_dict()
        result.get('users').append(dict(user_result, **{'turn': index == current_user_index - 1}))
    return json.dumps(result, ensure_ascii=False, indent=2)


@app.route('/add_user/<userID>')
def add_user(userID):
    global users
    users.append(User(name=userID, cards=[CARDS.get("B1"), CARDS.get("G2")], attractions=[CARDS.get("O1")]))


@app.route('/users')
def get_users():
    return Response(make_response(), mimetype="application/json")


@app.route('/')
def root():
    # result_str = "Roll: %d\nUser: %s\n" % (roll, users[pv].name)
    global current_user_index
    global last_roll
    # pv = current_user_index

    not_current_users = [user for index, user in enumerate(users) if index != current_user_index]
    current_user = users[current_user_index]
    not_current_users_sorted = sort(not_current_users, current_user.uid)
    roll = random.randint(1, 6)
    roll += random.randint(1, 6)
    last_roll = roll
    for index, user in enumerate(not_current_users_sorted):
        user.do_move_red(roll, current_user_index == index, current_user)

    for index, user in enumerate(users):
        user.do_move(roll, current_user_index == index)

    current_user_index += 1
    if current_user_index >= len(users):
        current_user_index = 0
        for user in users:
            user.buy_card = False
    return Response(make_response(), mimetype="application/json")


@app.route('/run/<int:number>')
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


@app.route('/card/<cardID>')
def addcard(cardID):
    global current_user_index
    cur_num_atr = 0
    if users[current_user_index].money >= CARDS.get(cardID).cost and \
            users[current_user_index].buy_card is False and CARDS.get(cardID).type != 4:
        users[current_user_index].add_card(CARDS.get(cardID))
        users[current_user_index].money += - CARDS.get(cardID).cost
        users[current_user_index].buy_card = True
        print(users[current_user_index].name, CARDS.get(cardID).name, 'Карточка добавлена')
    if users[current_user_index].money >= CARDS.get(cardID).cost and \
            users[current_user_index].buy_card is False and not (
            CARDS.get(cardID) in users[current_user_index].attractions):
        users[current_user_index].add_attractions(CARDS.get(cardID))
        users[current_user_index].money += - CARDS.get(cardID).cost
        users[current_user_index].buy_card = True
        print(users[current_user_index].name, CARDS.get(cardID).name, 'Карточка добавлена')
        for card in users[current_user_index].attractions:
            cur_num_atr += 1
        if cur_num_atr == 9:
            users[current_user_index].WIN = True
        if users[current_user_index].WIN is True:
            print(users[current_user_index].name, "ПОБЕДИТЕЛЬ!!!!")



    return Response(make_response(), mimetype="application/json")
