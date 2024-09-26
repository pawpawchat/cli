from inquirer import prompt, List, Text
import inquirer

def menu():
    questions = [List("action", "Hello, let's started", ["Login", "Register", "Exit"])]
    return prompt(questions)["action"] 

def sign_in():
    # questions = [Text("username", "Username:"), Text("password", "Password:")]
    questions = [Text("id", "ID")]
    return prompt(questions)

def sign_up():
    questions = [Text("first_name", "First name"), Text("second_name", "Second name")]
    return prompt(questions)
