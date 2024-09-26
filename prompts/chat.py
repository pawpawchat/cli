from inquirer import prompt, Text, List

def menu():
    questions = [List("action", "Action", ["Create", "Enter", "Exit"])]
    return prompt(questions)["action"]

def creating():
    questions = [Text("title", "Title")]
    return prompt(questions)["title"]

def enter():
    questions = [Text("chat_id", "Chat ID")]
    return prompt(questions)["chat_id"]

def chat_room():
    questions = [List("action", "Action", ["Send", "Reply", "Details", "Exit"])]
    return prompt(questions)["action"]

def details():
    questions = [List("action", "Action", ["Change title", "Change description", "Invite user", "Kick member", "Delete chat", "Exit"])]
    return prompt(questions)["action"]

def send_message():
    questions = [Text("body", "Text")]
    return prompt(questions)["body"]