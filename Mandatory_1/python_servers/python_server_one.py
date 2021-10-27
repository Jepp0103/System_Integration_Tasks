# from bottle import run
import requests
import csv


def send():
    while True:
        print("Enter number")
        number = input()
        xml = f"<?xml version='1.0' encoding='utf-8'?><data>{number}</data>"
        headers = {"Content-Type": "application/xml"}  # set what your server accepts
        response = requests.post(
            "http://127.0.0.1:2222/receive-xml", data=xml, headers=headers
        )
        readcsv(response.text.splitlines())


def readcsv(csvdata):
    reader = csv.reader(csvdata, delimiter=",")
    for row in reader:
        print(row)


send()

# run(host="127.0.0.1", port=1111, debug=False, reloader=True, server="paste")
