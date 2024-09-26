from inquirer import prompt, Text, List

def menu():
    #"Add avatar", "Change avatar", "Delete avatar",
    questions = [List("action", "Action", ["Update", "Delete", "Exit"])]
    return prompt(questions)["action"]

def update():
    questions = [List("action", "You want to change", ["Avatar", "Profile", "Cancel"])]
    return prompt(questions)["action"]

def update_data():
    questions = [Text("username", "Username"), Text("description", "Description"), Text("first_name", "First name"), Text("second_name", "Second name"), Text("birthday", "Birthday")]
    return prompt(questions)

def delete():
    questions = [List("action", "Profile data can not recover", ["Delete", "Cancel"])]
    return prompt(questions)["action"]
