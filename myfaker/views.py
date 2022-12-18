from django.shortcuts import render


def dummy(request):
    
    return render(request,'response.html')
