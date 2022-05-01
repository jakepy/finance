import plotly.express as px
import yfinance as yf
import pandas as pd
import numpy as np
import datetime as dt
import warnings
import altair as alt
warnings.simplefilter('ignore')

today = dt.date.today().strftime("%m-%d-%Y")

curr_stocks_csv = f'Input/unusual-stock-options-activity-{today}.csv'

past_stocks_csv = f'Input/unusual-stock-options-activity-{today}.csv'

df = pd.read_csv(curr_stocks_csv)
df.index += 1
df.dropna(inplace=True)
df.rename(columns={
    'Exp Date': 'Expiration',
    'Midpoint': 'Mid',
    'Open Int': 'OI',
    'DTE': 'Days to Exp',
    "Time": "Date"}, inplace=True)
df['Time'] = dt.datetime.today()
df['Expiration'] = pd.to_datetime(df['Expiration'])
df['Cash Value'] = (df['Volume'] * df['Last'] * 100).astype(int)
df['Price'] = df['Price'].astype(float)
df['Strike'] = df['Strike'].astype(float)
df['Volume'] = df['Volume'].astype(int)
df['Days to Exp'] = df['Days to Exp'].astype(int)
df['OI'] = df['OI'].astype(int)
df['Delta'] = df['Delta'].astype(float)
df = (df[['Symbol', 'Type', 'Price', 'Strike', 'Last', 'Expiration', 'Cash Value', 'Volume', 'OI', 'Vol/OI', 'IV', 'Delta', 'Days to Exp', 'Bid', 'Mid', 'Ask', 'Date']])
df = df.sort_values(by=(['Symbol', 'Expiration', 'Type', 'Cash Value']))

curr_etf_csv = f'Input/unusual-etf-options-activity-{today}.csv'

past_etf_csv = f'Input/unusual-etf-options-activity-01-06-2022.csv'

etf_df = pd.read_csv(past_etf_csv)
etf_df.index += 1
etf_df.dropna(inplace=True)
etf_df.rename(columns={
    'Exp Date': 'Expiration',
    'Midpoint': 'Mid',
    'Open Int': 'OI',
    'DTE': 'Days to Exp',
    "Time": "Date"}, inplace=True)
etf_df['Time'] = dt.datetime.today()
etf_df['Expiration'] = pd.to_datetime(etf_df['Expiration'])
etf_df['Cash Value'] = (etf_df['Volume'] * etf_df['Last'] * 100).astype(int)
etf_df['Price'] = etf_df['Price'].astype(float)
etf_df['Strike'] = etf_df['Strike'].astype(float)
etf_df['Volume'] = etf_df['Volume'].astype(int)
etf_df['Days to Exp'] = etf_df['Days to Exp'].astype(int)
etf_df['OI'] = etf_df['OI'].astype(int)
etf_df['Delta'] = etf_df['Delta'].astype(float)
etf_df = (etf_df[['Symbol', 'Type', 'Price', 'Strike', 'Last', 'Expiration', 'Cash Value', 'Volume', 'OI', 'Vol/OI', 'IV', 'Delta', 'Days to Exp', 'Bid', 'Mid', 'Ask', 'Date']])
etf_df = etf_df.sort_values(by=(['Symbol', 'Expiration', 'Type', 'Cash Value']))
