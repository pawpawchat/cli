import api.profile, pages.home, prompts.auth
from user import User
from json import loads

def menu(app):
    action = prompts.auth.menu() 
    if action == "Login":
        app.page = login

    elif action == "Register":
        app.page = register

    elif action == "Exit":
        app.page = None


def register(app):
    credentials = prompts.auth.sign_up()
    response, error = api.profile.create(credentials)
    if error is not None:
        app.page = menu
    else:
        user = loads(response)
        app.user = User(user["id"], user["username"])
        app.page = pages.home.menu
    return response


def login(app):
    credentials = prompts.auth.sign_in()
    #refactor this part when authorization will be ready
    response, error = api.profile.get_by_id(credentials["id"])
    if error is not None:
        app.page = menu
    else:
        user = loads(response)["profile"]
        app.user = User(user["id"], user["username"])
        app.page = pages.home.menu
    return response