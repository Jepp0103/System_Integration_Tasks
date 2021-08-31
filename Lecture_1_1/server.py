# Importing functions from the class bottle
from bottle import run, get, post, request


@get("/")  # Can use same method name because of the decorator
def do():
    return "X server 2"


@post("/signin")
def do():
    # Getting the form data
    name = request.forms.get("name")
    email = request.forms.get("email")
    return f"Hi {name}, your email is {email}. Server 2"


####################
run(host="127.0.0.1", port=4444, debug=True, reloader=True)
