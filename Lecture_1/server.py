# Importing functions from the class bottle
from bottle import run, get, post, request


@get("/")  # Can use same method name because of the decorator
def do():
    return "X server 1"


@post("/signin")
def do():
    # Getting the form data
    name = request.forms.get("name")
    email = request.forms.get("email")
    return f"Hi {name}, your email is {email}. Server 1"


####################
run(host="127.0.0.1", port=3333, debug=True, reloader=True)
