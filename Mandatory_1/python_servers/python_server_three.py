from bottle import request, run, post, response
import json
import csv
import io

hostname = "127.0.0.1"
port = 3333


@post("/receive-json")
def do():
    jsondata = json.load(request.body)
    print("Server 2 received json data:", jsondata)

    number = int(jsondata["data"]) * 3

    csv_data = [["data"], [number]]

    result = create_csv(csv_data)
    print("Data sent back to server 2:", result)
    response.content_type = "text/csv"
    return result


def create_csv(input):
    output = io.StringIO()
    writer = csv.writer(output, delimiter=",")
    writer.writerows(input)
    return output.getvalue()


run(host=hostname, port=port, debug=True, reloader=True, server="paste")
