import prompts.chat, pages.home, pages.chat, api.chat
from json import loads, dumps

#yeah i know
current_chat = None | str

def menu(app):
    print("--Chats--\n")
    response, error = api.chat.get_all(app.user.id)
    if error is not None:
        app.page = pages.home.menu
        return response
    
    chats = loads(response)["chats"]
    if chats != None:
        for chat in chats:
            print(f"{chat["id"]}@{chat["title"]}")
    else:
        print("No chats")

    print()
    action = prompts.chat.menu()
    if action == "Create":
        app.page = pages.chat.creating
    elif action == "Enter":
        app.page = pages.chat.enter_to_chat
    elif action == "Exit":
        app.page = pages.home.menu
    

def creating(app):
    title = prompts.chat.creating()
    data = {"title":title, "owner_id": app.user.id, "owner_username": app.user.username, "created_at": "2024-12-12T12:00:00Z"}
    response, error = api.chat.create(data)
    app.page = pages.chat.menu
    return response


def enter_to_chat(app):
    chat_id = prompts.chat.enter()
    response, error = api.chat.get_by_id(chat_id)
    
    if error is not None:
        app.page = pages.chat.menu
        return response
    
    pages.chat.current_chat = loads(response)
    app.page = pages.chat.chat_room


def chat_room(app):
    chat = pages.chat.current_chat
    print(f"--{chat["chat"]["title"]}--\n")
   
    messages = chat["messages"]
    if messages is not None:
        for message in messages:
            print(f"{message["message_id"]}@{message["sent_at"]}")
            print(f"[{message["sender_username"]}]")
            print(f"{message["body"]}\n")
    else:
        print("No messages\n")
   
    action = prompts.chat.chat_room()
    if action == "Send":
        app.page = send_message
   
    elif action == "Details":
        app.page = pages.chat.details
   
    elif action == "Exit":
        app.page = pages.home.menu


def send_message(app):
    text = prompts.chat.send_message()
    message = {
        "sender_id":app.user.id, 
        "sender_username":app.user.username, 
        "body":text, 
        "sent_at":"2022-12-12T11:11:00Z"
    }
    chat_id = pages.chat.current_chat["chat"]["id"]
    response, error = api.chat.send_message(chat_id, message)
    app.page = pages.chat.menu
    return response


def details(app):
    chat_id = pages.chat.current_chat["chat"]["id"]
    response, error = api.chat.get_members(chat_id)
    if error is not None:
        app.page = pages.chat.menu
        return response

    chat_info = {"chat": pages.chat.current_chat["chat"]} 
    if response is not None:
        chat_info["members"] = loads(response)["members"]
    else:
        chat_info["members"] = "" 
    
    print(dumps(chat_info, indent=4), "\n")
    action = prompts.chat.details()
    if action == "Change title":
        pass
    
    elif action == "Invite":
        pass

    elif action == "Kick":
        pass

    elif action == "Exit":
        app.page = pages.chat.chat_room