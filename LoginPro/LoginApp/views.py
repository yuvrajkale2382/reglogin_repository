from django.shortcuts import render
from .forms import RegForm,LoginForm
from .models import RegData
from django.http.response import HttpResponse
# Create your views here.

def Reg_view(request):
    if request.method == "POST":
        rform=RegForm(request.POST)
        if rform.is_valid():
            fname=request.POST.get('first_name','')
            lname=request.POST.get('last_name','')
            uname=request.POST.get('username','')
            pwd=request.POST.get('password','')
            mbl=request.POST.get('mobile','')
            eml=request.POST.get('email','')

            data=RegData(
                first_name=fname,
                last_name=lname,
                username=uname,
                password=pwd,
                mobile=mbl,
                email=eml
            )
            data.save()
            lform=LoginForm()
            return render(request,'LoginForm.html',{'lform':lform})
    else:
        rform=RegForm()
        return render(request,'RegForm.html',{'rform':rform})
def Login_view(request):
    if request.method=="POST":
        lform=LoginForm(request.POST)
        if lform.is_valid():
            uname=request.POST.get('username','')
            pwd=request.POST.get('password','')
            uname1=RegData.objects.filter(username=uname)
            pwd1=RegData.objects.filter(password=pwd)
            if uname1 and pwd1:
                return HttpResponse("<h1>Login Successfull</h1>")
            else:
                return HttpResponse("<h1>Invalid Username and Password</h1>")
        else:
            return HttpResponse("invalid data")
    else:
        lform=LoginForm()
        return render(request,'LoginForm.html',{'lform':lform})


