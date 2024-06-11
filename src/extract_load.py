import yfinance as yf
import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

commodities = ['CL=F', 'GC=F', 'SI=F']

def search_commodities_data(simbol, period = '5d', interval = '1d'):
  ticker = yf.Ticker('CL=F')
  data = ticker.history(period, interval)[['Close']]
  data['simbol'] = simbol
  return data

def search_all_data(commodities):
  datas = []
  for simbol in commodities:
    data = search_commodities_data(simbol)
    datas.append(data)
  return pd.concat(datas)

if __name__ == "__main__":
  concat_data = search_all_data(commodities)
  print(concat_data)

  
