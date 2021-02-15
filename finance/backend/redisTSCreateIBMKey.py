
import json
from user import return_data
import time
from datetime import datetime
from redistimeseries.client import Client 
rts = Client(host='127.0.0.1', port=6379)

company_symbol="IBM"
data = return_data("IBM")

rts.create('DAILYOPEN:IBM', labels={  'SYMBOL': 'IBM'
                             , 'DESC':'OPEN'
                             , 'TIMEFRAME': '1_DAY'
                             , 'COMPANYNAME': 'IBM'})

rts.create('DAILYHIGH:IBM', labels={  'SYMBOL': 'IBM'
                             , 'DESC':'HIGH'
                             , 'TIMEFRAME': '1_DAY'
                             , 'COMPANYNAME': 'IBM'})

rts.create('DAILYLOW:IBM', labels={  'SYMBOL': 'IBM'
                             , 'DESC':'LOW'
                             , 'TIMEFRAME': '1_DAY'
                             , 'COMPANYNAME': 'IBM'})

rts.create('DAILYCLOSE:IBM', labels={  'SYMBOL': 'IBM'
                             , 'DESC':'CLOSE'
                             , 'TIMEFRAME': '1_DAY'
                             , 'COMPANYNAME': 'IBM'})

dtFmt = '%Y-%m-%d'
epoch = datetime(1970, 1, 1)

dict_key={'1. open':'DAILYOPEN:IBM',
          '2. high':'DAILYHIGH:IBM',
          '3. low':'DAILYLOW:IBM',
          '4. close':'DAILYCLOSE:IBM',
          '5. adjusted close': 'DAILYADJCLOSE:IBM',
          '6. volume': 'DAILYVOL:IBM',
          '7. dividend amount': 'DAILYAMNT:IBM',
          '8. split coefficient': 'DAILYSPLIT:IBM',
         }
dict_price={}

for date in data['Time Series (Daily)']:
    for price_type in data['Time Series (Daily)'][date]:
        price_data = data['Time Series (Daily)'][date][price_type]
        add_price_data=( dict_key[price_type]
                        , int((datetime.strptime(str(date), dtFmt) - epoch).total_seconds()*1000)
                        , price_data)
        if price_type not in dict_price:
            dict_price[price_type]=[add_price_data]
        else:
            dict_price[price_type].append(add_price_data)

rts.madd(list(dict_price['1. open']))
rts.madd(list(dict_price['2. high']))
rts.madd(list(dict_price['3. low']))
rts.madd(list(dict_price['4. close']))
