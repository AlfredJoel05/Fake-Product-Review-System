from django.shortcuts import render
from .models import Concon
# Create your views here.
def contact(request):
    return render(request,'contact.html',{})
# Create your views here.
