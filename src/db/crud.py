from tinydb import TinyDB,where

usrtb=TinyDB('src/db/user.json').table('user')

def add(username,password,highscore):
    usrtb.insert({'username':username,'password':password,'high score':highscore})

def check_info(username,password):
    if usrtb.contains(where('username')==username):
        usr=usrtb.get(where('username')==username)
        if usr['password']==password:
            return True
    return False

def check_name(username):
    return usrtb.contains(where('username')==username)

def get_score(username):
    usr = usrtb.get(where('username') == username)
    return usr['high score']

def upd_score(username,score):
    usrtb.update({'high score':score},where('username')==username)