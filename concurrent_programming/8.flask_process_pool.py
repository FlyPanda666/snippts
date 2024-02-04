import flask
from concurrent.futures import ProcessPoolExecutor
import math
import json


app = flask.Flask(__name__)


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


@app.route("/is_prime/<numbers>")
def api_is_prime(numbers):
    number_list = [int(x) for x in numbers.split(",")]
    results = pool.map(is_prime, number_list)
    return json.dumps(dict(zip(number_list, results)))


if __name__ == "__main__":
    # 注意这里必须这么写.与thread不一样.
    pool = ProcessPoolExecutor()
    app.run()
