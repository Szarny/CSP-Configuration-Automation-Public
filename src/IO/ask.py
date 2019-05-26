from IO import pycolor
from IO import prompt_format

def ask(message: str) -> str:
    return input(prompt_format.prompt_format(pycolor.Pycolor.GREEN, "?", message + " >> "))
