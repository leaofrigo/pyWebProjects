import requests

# # example URL for total population
url='http://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?format=json'

# # request and save data in a dictionary "data"
data=requests.get(url).json()

# # verify data type
type(data[1][2])

# # verify dictionary length
len(data[1][:])

# # gets all years
years=[]
for i in range(1,len(data[1][:])):
    years.append(data[1][i]['date'])






import requests

# url to get metadata
url_meta='http://api.worldbank.org/v2/sources/2/country/data?format=json'
meta=requests.get(url_meta).json()

# number of countries in DB
nr_cnt=meta['total']

# create precise url string for API
url_nr_cnt='http://api.worldbank.org/v2/sources/2/country/data?format=json&per_page=%s' % (nr_cnt)
countries=requests.get(url).json()

# country ids
country_ids=[]
for i in range(0,nr_cnt):
    c_id = countries['source'][0]['concept'][0]['variable'][i]['id']
    c_name = countries['source'][0]['concept'][0]['variable'][i]['value']
    country_ids.append([c_id,c_name])
