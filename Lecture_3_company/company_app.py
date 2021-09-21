from bottle import run, get, view, post, request
import json
import jwt
import requests

##############################


@get("/")
@view("index.html")
def do():
    return dict(company_name="SUPER")


@get("/index-token")
@view("index_token.html")
def do():
    return dict(company_name="Token stuff")


@post("/get-name-by-cpr")
def do():
    # Connect to db
    # Execute a SQL/Document query
    data_from_client = json.load(request.body)
    print("cpr", data_from_client)
    cpr = data_from_client['cpr']
    file_name = "./data/" + cpr + ".txt"  # In python you go from the root
    opened_file = open(file_name, "r")
    return opened_file.read()


@post("/process-jwt-token")
def do():
    result = ""
    try:
        token = json.load(request.body)["jwt"]

        try:
            result = jwt.decode(
                token, "jwt-secret-key", algorithms=["HS256"])
        except Exception as jwt_error:
            send_sms(jwt_error)

        try:
            email = result["email"]
        except Exception as emailException:
            send_sms("Email missing")

    except Exception as json_error:
        send_sms(json_error)

    return str(result)


def send_sms(message):
    endpoint = "https://fatsms.com/api-send-sms"
    phone = "+4542659183"
    my_api_key = "7893f0d6872d606467a9e0e3a998d8db"
    data_dict = {"to_phone": phone, "api_key": my_api_key, "message": message}
    requests.post(endpoint, data = data_dict)
    print(str(data_dict))


    ##############################
run(host="127.0.0.1", port=4444, debug=True, reloader=True, server="paste")
