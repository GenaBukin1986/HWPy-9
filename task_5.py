from functools import wraps

def cash(func):
    my_dict = {}
    @wraps(func)
    def wrapper(*args, **kwargs):
        if func.__name__ == "fibonach" or func.__name__ == "factor":
            a, *_ = args
            if a in my_dict:
                return my_dict[a]
            else:
                my_dict[a] = func(a)
                return my_dict[a]
        print(f"Это другая функция и имя ее {func.__name__}")
        return func(*args, **kwargs)
            
    return wrapper


@cash
def fibonach(n: int) -> str:
    print(f"Вычисляю число Фибоначи для числа {n}")
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f"Число Фибоначи для {n} равно {f}"

@cash
def factor(n: int) -> int:
    if n <= 1:
        return n
    return factor(n - 1) * n

@cash
def new_fib(n: int) -> int:
    if n <= 1:
        return n
    return new_fib(n - 1) + new_fib(n - 2)

@cash
def func():
    return f"This is function {func.__name__}!"

if __name__ == "__main__":
    print(fibonach(5))
    print(fibonach(15))
    print(fibonach(25))
    print(fibonach(5))
    print(fibonach(5))
    print(fibonach(15))
    print("=" * 100)
    print(func())
    print(func())
    print(func())
    print(func())
    print(factor(5))
    print(factor(5))
    print(factor(5))
    print(factor(5))
    print(new_fib(6))
    print(new_fib(7))
    print(new_fib(6))