from bottle import run, post, request
import json
import csv
import io


@post("/receive-json")
def do():
  received_json = json.load(request.body)

  print("received json", received_json)
  
  
run(host="127.0.0.1", port=3333, debug=True, reloader=True, server="paste")