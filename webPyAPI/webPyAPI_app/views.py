from django.shortcuts import render

# # views to render home page template
def index_page(request):
    import requests
    # url to get metadata
    url_meta='http://api.worldbank.org/v2/sources/2/country/data?format=json'
    meta=requests.get(url_meta).json()

    # number of countries in DB
    nr_cnt=meta['total']

    # create precise url string for API
    url_nr_cnt='http://api.worldbank.org/v2/sources/2/country/data?format=json&per_page=%s' % (nr_cnt)
    countries=requests.get(url_nr_cnt).json()

    # country ids
    country_ids=[]
    for i in range(0,nr_cnt):
        c_id = countries['source'][0]['concept'][0]['variable'][i]['id']
        c_name = countries['source'][0]['concept'][0]['variable'][i]['value']
        country_ids.append([c_id,c_name])

    context = {'country_ids':country_ids,'numb_countries':nr_cnt}
    return render(request,'webPyAPI_app/index.html',context)

# # views to render about page template
def about_page(request):
    return render(request,'webPyAPI_app/about.html')

# # views to render code page template
def code_page(request):
    return render(request,'webPyAPI_app/code.html')

# # views to get API data
def get_data_API(request):
    import requests

    # url to get metadata
    url_meta='http://api.worldbank.org/v2/sources/2/country/data?format=json'
    meta=requests.get(url_meta).json()

    # number of countries in DB
    nr_cnt=meta['total']

    # create precise url string for API
    url_nr_cnt='http://api.worldbank.org/v2/sources/2/country/data?format=json&per_page=%s' % (nr_cnt)
    countries=requests.get(url_nr_cnt).json()

    # country ids
    country_ids=[]
    for i in range(0,nr_cnt):
        c_id = countries['source'][0]['concept'][0]['variable'][i]['id']
        c_name = countries['source'][0]['concept'][0]['variable'][i]['value']
        country_ids.append([c_id,c_name])

    context = {'country_ids':country_ids,'numb_countries':nr_cnt}
    return render(request,'webPyAPI_app/index.html',context)
