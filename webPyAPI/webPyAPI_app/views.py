from django.shortcuts import render

# # views to render home template
def index(request):
    context_dict = {'text':'hello world','number':100}
    return render(request,'webPyAPI_app/index.html',context_dict)

# # views to get API data
def get_data_API(request):
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
    print(years)
    return render(request,'webPyAPI_app/index.html')
