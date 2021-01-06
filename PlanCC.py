import requests, pandas, time
import matplotlib.pyplot as plt

# configuration
strUrl = "https://api.awattar.at/v1/marketdata"
strData = "data"
strStart = "start_timestamp"
strEnd = "end_timestamp"
strPrice = "marketprice"

# init variables
startData = []
endData = []
priceData = []
priceEval = []
mean = 0

r = requests.get(strUrl)

for d in range(len(r.json()[strData])):

    startData.append(r.json()[strData][d][strStart])
    endData.append(r.json()[strData][d][strEnd])
    priceData.append(r.json()[strData][d][strPrice])
    mean = mean + r.json()[strData][d][strPrice]

mean = mean / len(r.json()[strData])    

for p in range(len(priceData)):
    if priceData[p] > mean:
        priceEval.append('higher')
    elif priceData[p] <= mean:
        priceEval.append('lower')
    else:
        pass  

print(priceData)
print(priceEval)
print(mean)
print(startData[0]*(10**6))
print(time.time_ns())

print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(startData[0]*(10**-3))))
   
def GetDatafromAwattar(self):
    # Get data from Awattar API
    pass

def WriteToInfluxDB(self, pstrTimestamp as float, strValue as str):
    # Writes value to the influxDb using HTTP get method like described in https://docs.influxdata.com/influxdb/v1.8/guides/write_data/
    pass