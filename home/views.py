from django.shortcuts import render,HttpResponse

# Create your views here.*args
def index(request):
    return render(request,'index.html')
    # return HttpResponse("this is home")

def about(request):
    return render(request,'about.html')

def resources(request):
    return render(request,'resources.html')