# Webull Fintech API Data Extractor
A lightweight Python tool that automatically extracts real-time market data from Webull’s public API every **five minutes** and stores it in a structured Excel file.

---

## Overview
This project fetches data from the following Webull endpoint:
https://quotes-gw.webullfintech.com/api/bgw/market/topGainers?regionId=6&rankType=5min&pageIndex=1
The script is designed to run continuously, polling the API at 5-minute intervals and saving the latest market stats to an Excel file.

---

## Extracted Fields
From each API cycle, the following fields are captured:
- **symbol**
- **change**
- **last_price**
- **high**
- **low**
- **volume**
- **vibrateRatio**
- **pe**
- **market_cap**

This allows you to track short-term market movement and build simple analytics or dashboards.

---

## Output
All extracted data is saved in an Excel file

---

## How It Works
1. Sends a GET request to the Webull Market Top Gainers API  
2. Parses and extracts the required fields  
3. Appends the data to an Excel file (`all_output.xlsx`)  
4. Repeats this process automatically every 5 minutes

PS: Perfect for traders, researchers, or developers who need lightweight market monitoring.

