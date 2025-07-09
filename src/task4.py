import json
import logging

import requests

PATH_TO_LOG_FILE = "../logs/logs.txt"
log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(PATH_TO_LOG_FILE, mode="a", encoding="utf-8")
file_formatter = logging.Formatter("%(levelname)s %(message)s %(asctime)s")
file_handler.setFormatter(file_formatter)
log.addHandler(file_handler)


def get_users_list():
    """Функция получает список пользователей"""
    log.info("Request time: ")
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    with open("../data/user.json", mode="w", encoding="utf-8") as file:
        json.dump(response.json(), file)


if __name__ == "__main__":
    get_users_list()
