from functools import cache

@cache
def fibonach(n: int) -> str:
    print(f"Вычисляю число Фибоначи для числа {n}")
    f = 1
    for i in range(1, n + 1):
        f *= i
    return f"Число Фибоначи для {n} равно {f}"

if __name__ == "__main__":
    print(fibonach(5))
    print(fibonach(15))
    print(fibonach(5))
    print(fibonach(10))
    print(fibonach(5))
    print(fibonach(5))
    