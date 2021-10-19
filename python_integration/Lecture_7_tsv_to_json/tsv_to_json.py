import requests
import json

tsvEndpoint = "https://docs.google.com/spreadsheets/d/e/2PACX-1vRYbybiVenyLTJ39ysmw36TfyJWU8p9UK72f81LJ_eIo6vwsV9va_aWETMCgl8EXOefIzTRABU7DqRZ/pub?output=tsv"
data = [{}]


def convertTsvToJson(tsv):
    response = requests.get(tsv)
    tsvData = response.text
    print(tsvData)
    jsonArray = []

    jsonData = json.dumps(tsvData)
    for i in jsonData.split():
        jsonArray.append(i)

    print("jsonarray", jsonArray)

    # columns = firstline.split()
    # lines = tsvData.readlines()[1:]

    # for line in lines:
    #     values = line.split()
    #     entry = dict(zip(columns, values))
    #     data.append(entry)

    # json.dumps(data)
    # json.loads(data)


convertTsvToJson(tsvEndpoint)
