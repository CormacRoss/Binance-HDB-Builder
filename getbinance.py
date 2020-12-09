import os
import sys
import ccxt
import time
import argparse
import logging
import pandas as pd
from pathlib import Path

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-start',     type=str, required=True, help='Start date')
    parser.add_argument('-end',       type=str, required=True, help='End date')
    parser.add_argument('-symbol',    type=str, required=True, help='Symbol')
    parser.add_argument('-hdb',       type=str, required=True, help='HDB path')
    parser.add_argument('-replace',   type=str, default='0',   help='Replace or append data')
    parser.add_argument('-timeframe', type=str, default='1m',  help='Timeframe to download',
                        choices=['1m', '5m','15m', '30m','1h', '2h', '3h', '4h', '6h', '12h', '1d'])
    return parser.parse_args()

# Parse arguments
args = parse_args()

# KDB variables we will use later
q.ex = 'binance'
q.symbol = args.symbol
q.timeframe = q.string(args.timeframe)

# Python variables we will use later
exchange = getattr (ccxt, 'binance') ()
since = pd.date_range(start=args.start,end=args.end).astype(str)
minute = int(q('"j"$value ssr/[timeframe;("mhd");("*1";"*60";"*1440")]'))
limit = int(1440/minute)

# Check if the symbol is available on the Exchange
exchange.load_markets()
if args.symbol not in exchange.symbols:
    print('-'*36,' ERROR ','-'*35)
    print('The requested symbol ({}) is not available from {}\n'.format(args.symbol,'binance'))
    print('Available symbols are:')
    for key in exchange.symbols:
        print('  - ' + key)
    print('-'*80)
    quit()

# Get Binance data from CCXT
def ccxt_request(trade_date):
  start = exchange.parse_date(trade_date+ '00:00:00')
  candles = exchange.fetch_ohlcv(args.symbol, args.timeframe, start, limit)
  i = 0
  while len(candles) < limit:
    time.sleep(i)
    start = (minute*60000)+candles[-1][0]
    can = exchange.fetch_ohlcv(args.symbol, args.timeframe, start, limit-len(candles))
    candles = candles + can
    if 0==len(can): i += 1
  header = ['timestamp', 'open', 'high', 'low', 'close', 'volume']
  return pd.DataFrame(candles, columns=header)

# Convert Data Frame to KDB table
def kdb_cast(ohlc):
  t = q('!', ohlc.columns, ohlc.values.T).flip
  t = t.update('"P"$string"i"$timestamp%1e3')
  t = t.update('date:"d"$timestamp,sym:symbol,exchange:ex')
  t = q.xcols(['date','sym','exchange'],t)
  return t 

# Save data to KDB HDB
def kdb_save(trade_date,ohlc,hdb):
  q.hdb = ':' + hdb
  q.ohlc = ohlc
  q.date = trade_date
  q.date = q('"D"$ssr[string date;"-";"."]')
  q.path = q('.Q.dd[hdb;date,`ohlc]')
  if Path(q.path).is_dir() & (not int(args.replace)):
    q('path upsert .Q.en[hdb]ohlc')
    q('`sym`timestamp xasc path')
    q('@[;`sym;`p#]path')
  else:
    q('.Q.dpft[hdb;date;`sym;`ohlc]')
  print("Complete: {} {} data saved to: {}".format(args.timeframe,args.symbol,q.path))

# Request and save one date at a time
for td in since:
  ohlc = ccxt_request(td)
  ohlc = kdb_cast(ohlc)
  kdb_save(td,ohlc,args.hdb)

#import pdb; pdb.set_trace()
