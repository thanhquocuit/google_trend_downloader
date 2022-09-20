from pytrends.request import TrendReq

pytrends = TrendReq(hl='en-US', tz=420)

kw_list = ["bitcoin"]
pytrends.build_payload(kw_list, cat=0, timeframe='2015-01-01 2022-09-20', geo='CA', gprop='')

# return a pandas.DataFrame
result = pytrends.interest_over_time()

# dump to file
csv = result.to_csv()
with open('./save.csv', 'w') as file:
    file.write(csv)

print('Done')
