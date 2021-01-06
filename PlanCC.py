import requests, pandas

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
mean = 0

r = requests.get(strUrl)

for d in range(len(r.json()[strData])):

    startData.append(r.json()[strData][d][strStart])
    endData.append(r.json()[strData][d][strEnd])
    priceData.append(r.json()[strData][d][strPrice])
    mean = mean + r.json()[strData][d][strPrice]

mean = mean / len(r.json()[strData])    
print(priceData)
print(mean)
#print(pandas.Series.mean(priceData))