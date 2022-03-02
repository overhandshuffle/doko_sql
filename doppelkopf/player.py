import couchdb
import datetime
import uuid
from doppelkopf.database_constructors import User



def check_name(name):

    player_list = []
    for user in User.query.all():
        if user.username.startswith(name):
            player_list.append(
                {"username": user.username, "user_id": user.user_id})

    return player_list


def add_new_player(added_from, new_user):
    couch = couchdb.Server('http://admin:1234@localhost:5984/')
    db = couch['name']
    if user_already_exist(new_user, db):
        return "user already exists"
    data = {'_id': uuid.uuid4().__str__(), 'spieler': new_user, 'added_from': added_from,
            'created': datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")}
    db.save(data)

    return "player is now in database"


def user_already_exist(username, db):
    for docid in db.view('_all_docs'):
        i = docid['id']
        if db[i]['username'] == username:
            return True
        return False
