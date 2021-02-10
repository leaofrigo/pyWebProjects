from django.shortcuts import render
from django.http import HttpResponse
import requests
import json
# # views to render home page template
def index_page(request):
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

def check_data(request):
    # # dictionary that sends all data to the html page (template)
    context={}
    country_url = request.GET.get('country')
    indicator_url = request.GET.get('indicator')
    context = {'country':country_url,'indicator_code':indicator_url}
    # # url to get metadata
    # # check this data request manually to understand the received data structure
    url_data='http://api.worldbank.org/v2/country/%s/indicator/%s?format=json&per_page=100' % (country_url,indicator_url)
    data=requests.get(url_data).json()
    # # send data to the dictionary
    # # country name
    country_name=data[1][0]['country']['value']
    context['country_name']=country_name
    # # indicator name
    indicator=data[1][0]['indicator']['value']
    context['indicator']=indicator
    # # last evaluated year
    init_year=data[1][-1]['date']
    context['init_year']=init_year
    # # last evaluated ear
    final_year=data[1][0]['date']
    context['final_year']=final_year
    # # number of rows
    data_rows=data[0]['total']
    context['data_rows']=data_rows
    # # list with year and indicator value
    list_results=[]
    for i in range(0,len(data[1])):
       list_results.append([data[1][i]['date'],data[1][i]['value']])
    context['list_results']=(list_results)
    # # url to generate csv feature
    # # for local
    url_csv_data='/generate_csv/?country=%s&indicator=%s' % (country_url,indicator_url)

    context['url_csv_data']=(url_csv_data)
    return render(request,'webPyAPI_app/check_data.html',context)

def generate_csv(request):
    from pandas import DataFrame
    context={}
    country_url = request.GET.get('country')
    indicator_url = request.GET.get('indicator')
    context = {'country':country_url,'indicator_code':indicator_url}
    # # url to get metadata
    # # check this data request manually to understand the received data structure
    url_data='http://api.worldbank.org/v2/country/%s/indicator/%s?format=json&per_page=100' % (country_url,indicator_url)
    data=requests.get(url_data).json()
    # # send data to the dictionary
    # # list with year and indicator value
    list_results=[]
    for i in range(0,len(data[1])):
       list_results.append([data[1][i]['date'],data[1][i]['value']])
    results=DataFrame(list_results)
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=filename.csv'
    results.to_csv(path_or_buf=response,sep=';',float_format='%.2f',index=False,decimal=",")
    return response


def test_template(request):
    country_url = request.GET.get('country')
    indicator_url = request.GET.get('indicator')
    context = {'country':country_url,'indicator':indicator_url}
    return render(request,'webPyAPI_app/test_template.html',context)
