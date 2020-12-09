
# Binance HDB Builder

Binance HDB builder allows users to build a crypto currency KDB database in just a few minutes. The script can be used to collect the full price history of any crypto currency pair traded on Binance using the ccxt library.

This work was inspired by [Backtest Rookies.](https://backtest-rookies.com/2018/03/08/download-cryptocurrency-data-with-ccxt/)

# Requirements

This script requires the pyq and ccxt python libraries:

     pip install pyq
     pip install ccxt

# User Inputs

| Flag | Required | Description |
| :--- | :--- | :--- |
| start | Yes | Start date |
| end | Yes | End date |
| symbol | Yes | Currency pair |
| hdb | Yes | KDB HDB path |
| replace | No (default=0) | 0 = Append data to hdb, 1 = Replace/overwrite data |
| timeframe | No(default=1m) | Timeframe for data |

# Timeframe

The data returned will contains the OHLC prices within the specified timeframe along with the sum of the volume. The following time frames are available:

- 1m 
- 5m 
- 15m
- 30m
- 1h
- 2h
- 3h
- 4h
- 6h
- 12h
- 1d

# Example Use

Download 1m Bitcoin Data for all of 2020:

     ~:cross@host$ pyq getbinance.py -start 2020-01-01 -end 2020-12-01 -symbol BTC/USDT -hdb /home/cross/hdb -timeframe 1m -replace 0
     Complete: 1m BTC/USDT data saved to: :/home/cross/hdb/2020.01.01/ohlc
     Complete: 1m BTC/USDT data saved to: :/home/cross/hdb/2020.01.02/ohlc
     Complete: 1m BTC/USDT data saved to: :/home/cross/hdb/2020.01.03/ohlc
     ...

Add 1m Ethereum for all of 2020 to our HDB:

     ~:cross@host$ pyq getbinance.py -start 2020-01-01 -end 2020-12-01 -symbol ETH/USDT -hdb /home/cross/hdb -timeframe 1m -replace 0
     Complete: 1m ETH/USDT data saved to: :/home/cross/hdb/2020.01.01/ohlc
     Complete: 1m ETH/USDT data saved to: :/home/cross/hdb/2020.01.02/ohlc
     Complete: 1m ETH/USDT data saved to: :/home/cross/hdb/2020.01.03/ohlc
     ...

Now lets add 1m XRP to our HDB:

     ~:cross@host$ pyq getbinance.py -start 2020-01-01 -end 2020-12-01 -symbol XRP/USDT -hdb /home/cross/hdb -timeframe 1m -replace 0
     Complete: 1m XRP/USDT data saved to: :/home/cross/hdb/2020.01.01/ohlc
     Complete: 1m XRP/USDT data saved to: :/home/cross/hdb/2020.01.02/ohlc
     Complete: 1m XRP/USDT data saved to: :/home/cross/hdb/2020.01.03/ohlc
     ...

Lets overwite (replace=1) all 2020 KDB paritions with 5m XRP data, this will remove all the 1m we have just saved:

     ~:cross@host$ pyq getbinance.py -start 2020-01-01 -end 2020-12-01 -symbol XRP/ETH -hdb /home/cross/hdb -timeframe 1m -replace 1
     Complete: 1m XRP/ETH data saved to: :/home/cross/hdb/2020.01.01/ohlc
     Complete: 1m XRP/ETH data saved to: :/home/cross/hdb/2020.01.02/ohlc
     Complete: 1m XRP/ETH data saved to: :/home/cross/hdb/2020.01.03/ohlc
     ...

# Data

     ~:cross@host$ q hdb/
     KDB+ 4.0 2020.06.18 Copyright (C) 1993-2020 Kx Systems
     
     q)select from ohlc where date=2020.01.01
     date       sym      exchange timestamp                     open    high    low     close   volume
     ---------------------------------------------------------------------------------------------------
     2020.01.01 BTC/USDT binance  2020.01.01D00:00:00.000000000 7195.24 7196.25 7183.14 7186.68 51.64281
     2020.01.01 BTC/USDT binance  2020.01.01D00:01:00.000000000 7187.67 7188.06 7182.2  7184.03 7.248148
     2020.01.01 BTC/USDT binance  2020.01.01D00:02:00.000000000 7184.41 7184.71 7180.26 7182.43 11.68168
     2020.01.01 BTC/USDT binance  2020.01.01D00:03:00.000000000 7183.83 7188.94 7182.49 7185.94 10.02539
     2020.01.01 BTC/USDT binance  2020.01.01D00:04:00.000000000 7185.54 7185.54 7178.64 7179.78 14.9111
     2020.01.01 BTC/USDT binance  2020.01.01D00:05:00.000000000 7179.76 7182.51 7178.2  7179.99 12.46324
     2020.01.01 BTC/USDT binance  2020.01.01D00:06:00.000000000 7180    7182    7179.99 7182    3.573774
     2020.01.01 BTC/USDT binance  2020.01.01D00:07:00.000000000 7181.7  7183.77 7180.91 7183.66 14.47078
     2020.01.01 BTC/USDT binance  2020.01.01D00:08:00.000000000 7183.9  7187.74 7183.45 7187.68 12.84244
     2020.01.01 BTC/USDT binance  2020.01.01D00:09:00.000000000 7187.68 7191.77 7186.02 7191.07 16.01498
     2020.01.01 BTC/USDT binance  2020.01.01D00:10:00.000000000 7193.15 7193.53 7186.25 7187.36 12.60237
     2020.01.01 BTC/USDT binance  2020.01.01D00:11:00.000000000 7187.36 7191.08 7186.82 7188.71 10.26352
     2020.01.01 BTC/USDT binance  2020.01.01D00:12:00.000000000 7189.52 7189.52 7187    7187.02 2.860413
     2020.01.01 BTC/USDT binance  2020.01.01D00:13:00.000000000 7187.02 7187.02 7181.61 7182.08 13.23039
     2020.01.01 BTC/USDT binance  2020.01.01D00:14:00.000000000 7181.6  7182.1  7180.24 7180.97 9.111809
     ..

# Currency Pairs

When an invalid sym is entered all possible currency pairs on Binance will be displayed:

     ~:cross@host$ pyq getbinance.py -start 2020-01-01 -end 2020-12-01 -symbol INVALID/SYM  -hdb /home/cross/hdb  -timeframe 1m -replace 0
     ------------------------------------  ERROR  -----------------------------------
     The requested symbol (INVALID/SYM) is not available from binance
     
     Available symbols are:
       - AAVE/BKRW
       - AAVE/BNB
       - AAVE/BTC
       - AAVE/BUSD
       - AAVE/ETH
       - AAVE/USDT
       - AAVEDOWN/USDT
       - AAVEUP/USDT
       ...
