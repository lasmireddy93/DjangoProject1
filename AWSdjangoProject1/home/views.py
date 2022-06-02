from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'index.html')
    
def navbar(request):
    return render(request,'navbar.html')


def test(request):
    return render(request,'test.html')
    

def test2(request):
    return render(request,'test2.html')
    
def test3(request):
    return render(request,'test3.html')


def design2(request):
    return render(request,'index2.html')
    
    
def design3(request):
    contextvar = {
        'Variable1' : 'I am defined in view file using variable'
    }
    return render(request,'index3.html',contextvar)