from bottle import run, get, view, response

##############################
@get("/nemid")
@view("index_nem_id.html")
def do():
  return

##############################
run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")