from flask import Flask
from flask import request
import influxdb_client
from influxdb_client.client.write_api import SYNCHRONOUS

app = Flask(__name__)

@app.route("/api/temperature", methods=['POST'])
def temperature() :
    if request.method == 'POST':
        data = request.data

        lengthData = length(data)
        
        if len(lengthData) == 6 :
            firstDigits = getFirstDigits(lengthData)
            print(firstDigits)
            writeData("temp", firstDigits)
        elif len(lengthData) == 10 :
            firstDigits = getFirstDigits(lengthData)
            print(firstDigits)
            writeData("temp", firstDigits)
            lastDigits = getLastDigits(lengthData)
            print(lastDigits)
            writeData("temp", lastDigits)

        return data

@app.route("/api/humidity", methods=['POST'])
def humdity() :
    if request.method == 'POST':
        data = request.data

        lengthData = length(data)
        
        if len(lengthData) == 6 :
            firstDigits = getFirstDigits(lengthData)
            print(firstDigits)
            writeData("hum", firstDigits)
        elif len(lengthData) == 10 :
            firstDigits = getFirstDigits(lengthData)
            print(firstDigits)
            writeData("hum", firstDigits)
            lastDigits = getLastDigits(lengthData)
            print(lastDigits)
            writeData("hum", lastDigits)

        return data

def length(frame) :
    split1 = str(frame).split(":")
    split2 = split1[1].split("\"")
    return split2[1]

def getFirstDigits(frame) :
    return int(frame[2:6], 16) / 10

def getLastDigits(frame) :
    return int(frame[7:10], 16) / 10

def writeData(state, value) :
    bucket = "philly flingo"
    org = "philly flingo"
    token = "b38GF3tFRvgqCbsgQ9QAbUTqJSp9G5Mhl7o87QdO5cG7k8ooS3MymvZAp_nzhGD5bfcE2Tm3K5KL1iBJ6vco3g=="

    url="http://localhost:8086"

    client = influxdb_client.InfluxDBClient(
        url=url,
        token=token,
        org=org
    )

    write_api = client.write_api(write_options=SYNCHRONOUS)

    p = influxdb_client.Point("my_measures").field(state, value)
    write_api.write(bucket=bucket, org=org, record=p)