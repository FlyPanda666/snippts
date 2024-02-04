import math
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
import time


PRIMES = [112272535095293] * 100


def is_prime(number):
    if number < 2:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    sqrt_number = int(math.floor(math.sqrt(number)))
    for i in range(3, sqrt_number + 1, 2):
        if number % i == 0:
            return False
    return True


def single_thread():
    for number in PRIMES:
        is_prime(number)


def multi_thread():
    with ThreadPoolExecutor() as executor:
        executor.map(is_prime, PRIMES)


def mutli_process():
    with ProcessPoolExecutor() as executor:
        executor.map(is_prime, PRIMES)


if __name__ == "__main__":
    start = time.time()
    single_thread()
    end = time.time()
    print("single_thread costs: ", end - start)
    start = time.time()
    multi_thread()
    end = time.time()
    print("multi_thread costs: ", end - start)
    start = time.time()
    mutli_process()
    end = time.time()
    print("mutli_process costs: ", end - start)
