
# Binance HDB Builder

Binance HDB builder allows users to build a crypto currency KDB database in just a few minutes. The script can be used to collect the full history for any crypto currency pair traded on Binance.

This work was inspired by [Backtest Rookies.](https://backtest-rookies.com/2018/03/08/download-cryptocurrency-data-with-ccxt/)

# Requirements

This script requires the pyq python library:

     pip install pyq

# User inputs

| Flag | Required | Description |
| :--- | :--- | :--- |
| start | Yes | Start date |
| end | Yes | End date |
| symbol | Yes | Currency pair |
| hdb | Yes | KDB HDB path |
| replace | No (default=0) | 0 = Append data to hdb, 1 = Replace/overwrite data |
| timeframe | Yes | Timeframe for data |

# Example

Download 1m Bitcoin Data for all of 2020:

     ~:cross@host$ pyq .getbinance.py -start 2020-01-01 -end 2020-12-01 -symbol BTC/USDT  -hdb /home/cross/hdb  -timeframe 1m -replace 0
     Complete: 1m BTC/USDT data saved to: :/home/cross/hdb/2020.01.01/ohlc
     Complete: 1m BTC/USDT data saved to: :/home/cross/hdb/2020.01.02/ohlc
     Complete: 1m BTC/USDT data saved to: :/home/cross/hdb/2020.01.03/ohlc
     ...

Add 2020 1m Ethereum to our HDB:

     ~:cross@host$ pyq getbinance.py -start 2020-01-01 -end 2020-12-01 -symbol ETH/USDT  -hdb /home/cross/hdb  -timeframe 1m -replace 0
     Complete: 1m ETH/USDT data saved to: :/home/cross/hdb/2020.01.01/ohlc
     Complete: 1m ETH/USDT data saved to: :/home/cross/hdb/2020.01.02/ohlc
     Complete: 1m ETH/USDT data saved to: :/home/cross/hdb/2020.01.03/ohlc
     ...

Lets overwite (replace=1) all 2020 KDB paritions with 5m XRP data:

     ~:cross@host$ pyq getbinance.py -start 2020-01-01 -end 2020-12-01 -symbol XRP/ETH  -hdb /home/cross/hdb  -timeframe 1m -replace 0
     Complete: 1m XRP/ETH data saved to: :/home/cross/hdb/2020.01.01/ohlc
     Complete: 1m XRP/ETH data saved to: :/home/cross/hdb/2020.01.02/ohlc
     Complete: 1m XRP/ETH data saved to: :/home/cross/hdb/2020.01.03/ohlc
     ...
