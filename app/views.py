from django.shortcuts import render

# Create your views here.
def data_render(request):
    data='this is the data asumpution'
    d={'assumpution':data}
    return render(request,'data_render.html',context=d)
def login(request):
    d={'username':'ashu'}
    return render(request,'login.html',context=d)