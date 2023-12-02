from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'pages/index.html')


def dashboard(request):
    return render(request, 'rv/dashboard.html')