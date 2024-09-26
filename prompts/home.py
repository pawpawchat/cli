from inquirer import prompt, List

def menu():
    questions = [List("action", "Choose an option", ["Profile", "Chat", "Sign out", "Exit"])]
    return prompt(questions)["action"]
