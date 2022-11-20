from django.shortcuts import render

def infoDecide(request):
    return render(request, 'nuevaInfo/infoDecide.html')

def infoEgc(request):
    return render(request, 'nuevaInfo/infoEgc.html')
