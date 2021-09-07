from bottle import run, get, view, post, request
import json

##############################
@get("/")
@view("index.html")
def do():
  return dict(company_name = "SUPER")

@post("/get-name-by-cpr")
def do():
  #Connect to db
  #Execute a SQL/Document query
  data_from_client = json.load(request.body)
  print("cpr", data_from_client)
  cpr = data_from_client['cpr']
  file_name = "./data/" + cpr + ".txt"
  opened_file = open(file_name, "r")
  return opened_file.read()
  

##############################
run(host="127.0.0.1", port=4444, debug=True, reloader=True, server="paste")