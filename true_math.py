import math


def divide(first, second):
    if second == 0:
        return f'Из высшей математики деление числа {first} на {second} = {math.inf}'
    else:
        return f'Деление числа {first} на {second} = {first / second}' #first / second