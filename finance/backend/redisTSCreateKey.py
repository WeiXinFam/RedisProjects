from redistimeseries.client import Client 
rts = Client(host='127.0.0.1', port=6379)

# Create Time Series and the aggregated time series
rts.create('DAILYRSI:GS',
            labels={
                'SYMBOL': 'GS',
                'DESC': 'RELATIVE_STRENGTH_INDEX',
                'INDEX': 'DJIA',
                'TIMEFRAME': '1_DAY',
                'INDICATOR': 'RSI',
                'COMPANYNAME': 'GOLDMAN_SACHS_GROUP'
            })

rts.create('INTRADAYPRICES:GS',
            labels={
                'SYMBOL': 'GS',
                'DESC': 'SHARE_PRICE',
                'INDEX': 'DJIA',
                'PRICETYPE':'INTRADAY',
                'COMPANYNAME': 'GOLDMAN_SACHS_GROUP'
            })

rts.create('DAILYRSI15MINRNG:GS',
            labels={
                'SYMBOL': 'GS',
                'DESC': 'RELATIVE_STRENGTH_INDEX',
                'INDEX': 'DJIA',
                'TIMEFRAME': '15_MINUTES',
                'AGGREGATION': 'RANGE',
                'INDICATOR': 'RSI',
                'COMPANYNAME': 'GOLDMAN_SACHS_GROUP'
            })
            # 900 = 60 seconds * 15 min
rts.createrule('DAILYRSI:GS','DAILYRSI15MINRNG:GS','range',900)

rts.create('INTRADAYPRICES15MINRNG:GS',
            labels={
                'SYMBOL': 'GS',
                'DESC': 'SHARE_PRICE',
                'INDEX': 'DJIA',
                'PRICETYPE':'RANGE',
                'AGGREGATION': 'RANGE',
                'DURATION': '15_MINUTES',
                'COMPANYNAME': 'GOLDMAN_SACHS_GROUP'
            })
rts.createrule('INTRADAYPRICES:GS','INTRADAYPRICES15MINRNG:GS','range',900)

rts.create('INTRADAYPRICES15MINSTDP:GS',
            labels={
                'SYMBOL': 'GS',
                'DESC': 'SHARE_PRICE',
                'INDEX': 'DJIA',
                'PRICETYPE':'STDDEV',
                'AGGREGATION': 'STDDEV',
                'DURATION': '15_MINUTES',
                'COMPANYNAME': 'GOLDMAN_SACHS_GROUP'
            })
rts.createrule('INTRADAYPRICES:GS','INTRADAYPRICES15MINSTDP:GS','std.p',900)

# Populate Data
rts.madd(<RSIIndicatorList>)

# Querying data
rts.range( 'INTRADAYPRICES15MINRNG:GS' 
         , from_time = 1603704600 
         , to_time   = 1603713600)
        #  Start is 9:30 a.m. on October 26, 2020 ET

allRSIValues = rts.mget(filters=['DESC=RELATIVE_STRENGTH_INDEX','TIMEFRAME=1_DAY'], with_labels=False)
