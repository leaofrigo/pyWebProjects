from django.shortcuts import render

# Create your views here.
def index(request):
    context_dict = {'text':'hello world','number':100}
    return render(request,'webPyAPI_app/index.html',context_dict)
