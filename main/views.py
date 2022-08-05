from django.shortcuts import render
# Create your views here.
def index(reguest):
    return render(reguest,'main/index.html')

def numver(reguest):
    return render(reguest, 'main/number.html')



git remote add origin https://github.com/sultanaliev-adilet/django.git