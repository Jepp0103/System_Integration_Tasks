from bottle import request, run, post, response
import xml.etree.ElementTree as ET


hostname = "127.0.0.1"
port = 3333


@post("/xml-to-json")
def converXmlToJson():
    xml_data = request.body
    tree = ET.parse(xml_data)
    root = tree.getroot()
    msg = root.text.strip()

    print(msg)


def convertToJson(input):

    return ""


run(host=hostname, port=port, debug=True, reloader=True, server="paste")
