from django.shortcuts import render

# Create your views here.
def Signup(request):
    return render(request,"signup.html")

def Panpage(request):
    return render(request,"pan.html")

def Kycpage(request):
    return render(request,"kyc.html")

def Notpan(request):
    return render(request,"notpan.html")
def Mail(request):
    return render(request,"mail.html")

