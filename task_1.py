from functools import wraps

def how_are_you(fun):
    @wraps(fun)
    def wrapper(*args, **kwargs):
        input("How are you? ")
        print("I am fine!")
        res = fun(*args, **kwargs)
        return res
    return wrapper

@how_are_you
def func(a: int, b: int):
    """Функция для возведения a числа в степень b"""
    return a ** b

@how_are_you
def test():
    """This is First programm"""
    return "Hello world!"

if __name__ == "__main__":
    print(func(4, 5))
    help(func)
    print(test())