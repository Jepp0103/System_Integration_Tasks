from bottle import request, run, post, response
import csv
import io
import xml.etree.ElementTree as ET

hostname = "127.0.0.1"
port = 3333


@post("/xml-to-csv")
def converXmlToCsv():
    xml_data = request.body
    tree = ET.parse(xml_data)
    root = tree.getroot()
    msg = root.text.strip()

    print("message:", msg)
    csv_data = ["message", msg]

    result = convertToCsv(csv_data)
    print("Converted CSV:", result)
    response.content_type = "text/csv"
    return result


def convertToCsv(input):
    output = io.StringIO()
    writer = csv.writer(output, delimiter=",")
    writer.writerow(input)
    return output.getvalue()


run(host=hostname, port=port, debug=True, reloader=True, server="paste")
