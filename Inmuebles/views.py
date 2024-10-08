from django.shortcuts import render

# Create your views here.
def inmuebles(request):
    return render(request, 'inmuebles.html')