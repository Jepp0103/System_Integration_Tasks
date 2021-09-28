import requests

endpoint = "https://fatsms.com/api-send-sms"

my_api_key = "7893f0d6872d606467a9e0e3a998d8db"

while(True):
    print("Enter phone number: ")
    phone = input()

    print("Enter message: ")
    message = input()

    data_dict = {"to_phone": phone, "api_key": my_api_key, "message": message}

    response = requests.post(endpoint, data = data_dict)

    print("response from server:", str(response.text))
