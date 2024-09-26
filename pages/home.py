import pages.auth, pages.profile, pages.chat
import prompts.home

def menu(app):
    action = prompts.home.menu()

    if action == "Profile":
        app.page = pages.profile.menu

    elif action == "Chat":
        app.page = pages.chat.menu
    
    elif action == "Sign out":
        app.page = pages.auth.menu

    elif action == "Exit":
        app.page = None
    