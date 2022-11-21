from django.shortcuts import render

def infoDecide(request):
    return render(request, 'nuevaInfo/infoDecide.html')

def infoEgc(request):
    return render(request, 'nuevaInfo/infoEgc.html')

def infoTraducciones(request):
    return render(request, 'nuevaInfo/infoTraducciones.html')

def infoJornadas(request):
    return render(request, 'nuevaInfo/infoJornadas.html')
