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
