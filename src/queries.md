
# World Bank queries example


## Structure of a query:

``` http://api.worldbank.org/v2/country/all/indicator/SP.POP.TOTL?date=2010:2015&per_page=3000```

The parameters are separated by "&".

Number of rows per page
* per_page=123

Output format:
* format=json or xml > Output data format

Specify evaluation period
* date=2010:2015


## Request all countries in World Bank database:
http://api.worldbank.org/v2/sources/2/country/data?format=json

```import requests```
```# url to get metadata```
```url_meta='http://api.worldbank.org/v2/sources/2/country/data?format=json'```
```meta=requests.get(url).json()```
```# number of countries in DB```
```nr_cnt=meta['total']```
```# create precise url string for API```
```url_nr_cnt='http://api.worldbank.org/v2/sources/2/country/data?format=json&per_page=%s' % (nr_cnt)```
