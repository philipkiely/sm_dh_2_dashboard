from django.shortcuts import render
from .models import Employee

# Create your views here.
def index(request):
    return render(request, "index.html", {"employees": Employee.objects.all()})