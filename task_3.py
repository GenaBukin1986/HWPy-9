from json import dump, load
from functools import wraps

def count(num: int):    
    def decorater(func):
        counter = 0
        @wraps(func)
        def wrapper(*args, **kwargs):
            nonlocal counter
            for i in range(num):
                res = func(*args, **kwargs)
                counter+= 1
            return res, f'Функция была вызвана {counter}'
        
        return wrapper
    return decorater


def new_decor(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        res = func(*args, **kwargs)
        return res, f"Функция вызвана {wrapper.count}"
    wrapper.count = 0
    return wrapper

@new_decor
@count(3)
def function(a: int, b: int) -> str:
    return f"Периментр прямоугольника со сторанами {a} и {b} равен {(a + b) * 2}"

@new_decor
def hello():
    return "Hello world"

if __name__ == "__main__":
    # print(function(4, 5))
    # print(function(4, 5))
    # print(function(4, 5))
    print(hello())
    print(hello())
    print(hello())
    print(hello())
