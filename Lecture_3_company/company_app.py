from bottle import run, get, view, post, request
import json
import jwt

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
    email = ""
    phone = ""
    token = ""
    try:
        token = json.load(request.body)["jwt"]
        # print("token: " + (token))

        try:
            email = token["email"]
        except Exception:
            send_sms("Email missing")

        try:
            decoded_token = jwt.decode(
                token, "jwt-secret-key", algorithms=["HS256"])
        except Exception as jwt_error:
            send_sms(jwt_error)

        # print("decoded " + str(decoded_token))  # Returned as a dictionary

    except Exception as json_error:
        send_sms(json_error)

    return str(decoded_token)


def send_sms(message):
    phone = "+4542659183"


    ##############################
run(host="127.0.0.1", port=4444, debug=True, reloader=True, server="paste")
