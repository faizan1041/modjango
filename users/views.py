from django.shortcuts import render
from models import User

# Create your views here.

def index(request):
    employee = User.objects.create(
        email="abc@123.com",
        first_name="abc",
        last_name="def"
    )
    employee.save()
    return employee