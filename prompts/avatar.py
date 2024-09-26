from inquirer import prompt, Text, List

def menu():
    questions = [List("action", "Action", ["New", "Select", "Delete", "Cancel"])]
    return prompt(questions)

def new():
    questions = [Text("orig_url", "URL of the new avatar"), Text("added_at", "Added at")]
    return prompt(questions)

def select():
    questions = [Text("selected_avatar_id", "ID of the Avatar being selected")]
    return prompt(questions)

def delete():
    questions = [Text("deleted_avatar_id", "ID of the Avatar being deleted")]
    return prompt(questions)

