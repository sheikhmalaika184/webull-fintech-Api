import requests
import json
import pandas as pd
import time

PAGESIZE = 200
column_names = ['Symbol', '% Chg in 5Mins', 'Last Price', 'High', 'Low', 'Volume', '% Range', 'P/E', 'Market Cap']

def all_data():
  url = f"https://quotes-gw.webullfintech.com/api/bgw/market/topGainers?regionId=6&rankType=5min&pageIndex=1&pageSize={PAGESIZE}"

  payload = ""
  headers = {}

  response = requests.request("GET", url, headers=headers, data=payload)

  data = json.loads(response.text)
  data = data["data"]
  df = pd.DataFrame(columns=column_names)
  # getting data
  for i in range(len(data)):
    try:
      symbol = data[i]["ticker"]["symbol"]
      last_price = data[0]["ticker"]["close"]
      high = data[i]["ticker"]["high"]
      low = data[i]["ticker"]["low"]
      volume = data[i]["ticker"]["volume"]
      range1 = str(float(data[i]["ticker"]["vibrateRatio"])*100) + "%"
      pe = data[i]["ticker"]["peTtm"]
      market_cap = data[i]["ticker"]["marketValue"]
      change = float(data[i]["values"]["changeRatio"])*100
      df = df.append(pd.Series([symbol,change,last_price,high,low,volume,range1,pe,market_cap], index=df.columns), ignore_index=True)
      print(df)
    except:
      pass
  excel_filename = 'all_output.xlsx'
  # Write the DataFrame into the Excel file
  df.to_excel(excel_filename, index=False)


def one_percent_data():
  url = f"https://quotes-gw.webullfintech.com/api/bgw/market/topGainers?regionId=6&rankType=5min&pageIndex=1&pageSize={PAGESIZE}"

  payload = ""
  headers = {}

  response = requests.request("GET", url, headers=headers, data=payload)

  data = json.loads(response.text)
  data = data["data"]
  df = pd.DataFrame(columns=column_names)
  # getting data
  for i in range(len(data)):
    try:
      symbol = data[i]["ticker"]["symbol"]
      last_price = data[0]["ticker"]["close"]
      high = data[i]["ticker"]["high"]
      low = data[i]["ticker"]["low"]
      volume = data[i]["ticker"]["volume"]
      range1 = str(float(data[i]["ticker"]["vibrateRatio"])*100) + "%"
      pe = data[i]["ticker"]["peTtm"]
      market_cap = data[i]["ticker"]["marketValue"]
      change = float(data[i]["values"]["changeRatio"])*100
      if(change > 1):
        df = df.append(pd.Series([symbol,change,last_price,high,low,volume,range1,pe,market_cap], index=df.columns), ignore_index=True)
    except:
      pass
  excel_filename = 'one_percent_output.xlsx'
  # Write the DataFrame into the Excel file
  df.to_excel(excel_filename, index=False)

while True:
  all_data()
  #one_percent_data()
  time.sleep(300)