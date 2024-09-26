import pages.auth, prompts.profile, pages.home, api.profile

def menu(app):
    response, error = api.profile.get_by_id(app.user.id)
    if error is not None:
        app.page = pages.auth.menu
        return response        

    print(response, "\n")
    
    action = prompts.profile.menu()
    if action == "Exit":
        app.page = pages.home.menu
