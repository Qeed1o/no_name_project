import json
import random
from flask import Flask, Response
from User import User
from CARDS import CARDS
from Utils import sort

# from Utils import get_key

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

first_user = User(name="test1", cards=[CARDS.get("B1"), CARDS.get("G12")], attractions=[CARDS.get("O1"), CARDS.get("O2"), CARDS.get("O5")], uid=1)
second_user = User(name="test2", cards=[CARDS.get("R3"), CARDS.get("R4")], attractions=[CARDS.get("O1"), CARDS.get("O1")], uid=2)
third_user = User(name="test3", cards=[CARDS.get("R5"), CARDS.get("R6")], attractions=[CARDS.get("O1")], uid=3)
fourth_user = User(name="test4", cards=[CARDS.get("R7"), CARDS.get("R7")], attractions=[CARDS.get("O1"), CARDS.get("O2"), CARDS.get("O5")], uid=4)
current_user_index = -1
users = [first_user, second_user, third_user, fourth_user]


@app.route('/add_user/<userID>')
def add_user(userID):
    global users
    users.append(User(name=userID, cards=[CARDS.get("B1"), CARDS.get("G2")], attractions=[CARDS.get("O1")]))


@app.route('/user/<userID>')
def get_user(userID):
    is_user_turn = False
    found_user = None
    for index, user in enumerate(users):
        if user.name == userID:
            found_user = user
            if index == current_user_index:
                is_user_turn = True
        else:
            continue

    if found_user is None:
        return Response({"error": "Poshel naxui"}, mimetype="application/json")

    result_str = json.dumps({
        'turn': is_user_turn,
        'user': found_user.to_dict(),
    }, ensure_ascii=False)

    return Response(result_str, mimetype="application/json")

"""

{
    users: [{
        cards: [...],
        money: 10,
        name: "test1"
        }, ...],
    roll: 
    current
    
    
}


"""


@app.route('/')
def root():
    # result_str = "Roll: %d\nUser: %s\n" % (roll, users[pv].name)
    global current_user_index
    # pv = current_user_index
    current_user_index += 1
    if current_user_index >= len(users):
        current_user_index = 0
        for user in users:
            user.buy_card = False
    not_current_users = [user for index, user in enumerate(users) if index != current_user_index]
    current_user = users[current_user_index]
    not_current_users_sorted = sort(not_current_users, current_user.uid)
    # roll = random.randint(1, 6)
    roll = random.randint(12, 12)
    for index, user in enumerate(not_current_users_sorted):
        index += 1
        user.do_move_red(roll, current_user_index == index, current_user)

    for index, user in enumerate(users):
        user.do_move(roll, current_user_index == index)

    result_str = "%d,\n" % roll
    for index, user in enumerate(users):
        result_str += json.dumps({
            "name": user.name,
            "money": user.money,
            "turn": current_user_index == index,
            "cards": [card.name.encode().decode('utf-8') for card in user.cards]
        }, indent=4, ensure_ascii=False) + ',\n'
    return Response(result_str, mimetype="application/json")




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
    if users[current_user_index].money >= CARDS.get(cardID).cost and \
            users[current_user_index].buy_card is False and CARDS.get(cardID).type != 4:
        users[current_user_index].add_card(CARDS.get(cardID))
        users[current_user_index].money += - CARDS.get(cardID).cost
        users[current_user_index].buy_card = True
        return CARDS.get(cardID).name + '-Карточка добавлена'
    if users[current_user_index].money >= CARDS.get(cardID).cost and \
            users[current_user_index].buy_card is False:
        users[current_user_index].add_attractions(CARDS.get(cardID))
        users[current_user_index].money += - CARDS.get(cardID).cost
        users[current_user_index].buy_card = True
        return CARDS.get(cardID).name + '-Карточка ДОСТОПРИМЕЧАТЕЛЬНОСТИ добавлена'
    elif users[current_user_index].buy_card is False:
        return 'У вас недостаточно денег('
    elif current_user_index == -1:
        return 'Игра еще не началась))'
    else:
        return 'Вы уже купили карту на этом ходу('


"""

В 6:00 ДОЛЖНО быть готово:
Хоть какие-то карточки рабочие
Чтобы мы подключили фронтенд и оно не сваливалось
Мы бы могли сыграть основную часть игры (покупка карточек chek
, карточки отрабатывают(не обязательно все))

"""