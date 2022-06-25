# Various functions used across multiple 100 days projects.
from os import system, name

def clear():
    """Check OS and then clear terminal screen"""
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux
    else:
        _ = system('clear')
