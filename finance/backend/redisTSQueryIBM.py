import json
from user import data
import time
from datetime import datetime
from redistimeseries.client import Client 
rts = Client(host='127.0.0.1', port=6379)


dailyRange = rts.range(  'DAILYOPEN:IBM'
                                , from_time = 0
                                , to_time = 1611014400000)

print('****************IBM RANGE**************************************')
print(dailyRange)
print('****************IBM RANGE**************************************')

