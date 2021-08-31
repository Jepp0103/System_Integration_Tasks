# Importing functions from the class bottle
from bottle import run, get, post, request
import time
import requests
import threading


def timer():
    while True:
        result = requests.get("http://127.0.0.1:4444")
        print(result.text)
        time.sleep(1)


@get("/")  # Can use same method name because of the decorator
def do():
    return "X server 1"


@post("/letter")
def do():
    letter = request.forms.get("letter")
    if letter in ("a", "b", "c"):
        return f"Yes I got the letter: {letter}"
    else:
        req = int(requests.get("http://127.0.0.1:4444").text)
        print(f"Number: {req}")
        req_multiply = req * 2
        return str(req_multiply)


@post("/signin")
def do():
    # Getting the form data
    name = request.forms.get("name")
    email = request.forms.get("email")
    return f"Hi {name}, your email is {email}"


# xtimer = threading.Thread(target=timer)  # Targeting the method name timer.
# xtimer.start()

run(host="127.0.0.1", port=3333, debug=True, reloader=True)
