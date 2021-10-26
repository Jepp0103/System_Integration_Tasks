from bottle import request, run, post, response
import csv
import io
import xml.etree.ElementTree as et
import pandas as pd

hostname = "127.0.0.1"
port = 3333


@post("/xml-to-csv")
def converXmlToCsv():
    request_body = request.body.read()
    print("type", type(request_body))
    print("body:", request_body)
    xml_data = request_body.decode("utf-8")
    print("xml data:", xml_data)
    converted_data = et.parse(xml_data).getroot()

    print(converted_data.attrib)

    # csv_data = [["data"], [xml_data]]

    # result = convertToCsv(csv_data)
    # print("Converted CSV:", result)
    # response.content_type = "text/csv"

    # return result


def convertToCsv(input):
    output = io.StringIO()
    writer = csv.writer(output, delimiter=",")
    writer.writerows(input)
    return output.getvalue()


run(host=hostname, port=port, debug=True, reloader=True, server="paste")
