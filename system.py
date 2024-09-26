from os import system, name

def clear_terminal():
    system('clear' if name == 'posix' else 'cls')
