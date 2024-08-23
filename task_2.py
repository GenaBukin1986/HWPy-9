from functools import wraps
from time import sleep

def decorator(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        sleep(2)
        res = fun(*args, **kwargs)
        return res
    return wrapper

@decorator
def func(a: int, b: int):
    """Функция для возведения a числа в степень b"""
    return a ** b

@decorator
def test():
    """This is First programm"""
    return "Hello world!"

if __name__ == "__main__":
    print(func(3, 4))
    print(test())