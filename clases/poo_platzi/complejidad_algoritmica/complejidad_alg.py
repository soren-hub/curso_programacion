import time


def factorial(n):
    respuesta = 1

    while n > 1:
        respuesta *= n
        n -= 1
    return respuesta


def factorial_recur(n):
    if n == 1:
        return 1
    return n * factorial_recur(n - 1)


if __name__ == '__main__':
    n = 5000000
    comienzo = time.time()
    # print(factorial(n))
    final = time.time()
    print(final - comienzo)

    comienzo = time.time()
    # print(factorial_recur(n))
    final = time.time()
    print(final - comienzo)
