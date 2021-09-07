from bottle import run, get, view, response

##############################
@get("/")
@view("index.html")
def do():
  return

##############################
run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")