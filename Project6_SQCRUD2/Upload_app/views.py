from django.shortcuts import render,redirect
from .models import Candidate_Profile
from django.contrib import messages
# Create your views here.

def Lets_Register(request):
    if request.method == 'POST':
        Uname       = request.POST['name']
        Ugender     = request.POST['gender']
        Updf_file   = request.FILES['updf']
        Uexcel_file = request.FILES['uexcel']
        Uimage      = request.FILES['uimage']

        print("Name:",Uname,Ugender)
        
        mycan             = Candidate_Profile()
        mycan.Cname       = Uname
        mycan.Cgender     = Ugender
        mycan.Cpdf_file   = Updf_file
        mycan.Cexcel_file = Uexcel_file
        mycan.Cimage      = Uimage
        mycan.save()

    
        messages.success(request,"Successfully Registered")
        
        #return render(request,"Upload_app/1register.html")   
        return redirect("dis_view") 
    return render(request,"Upload_app/1register.html")

def Lets_View(request):
    vdata = Candidate_Profile.objects.all()
    if vdata:
        return render(request,"Upload_app/2display.html",{"viewdata":vdata})
    return render(request,"Upload_app/2display.html")

def Lets_update(request,cid):
    udata = Candidate_Profile.objects.get(id=cid)
    if request.method == 'POST':
        Uname       = request.POST['name']
        Ugender     = request.POST['gender']
        Updf_file   = request.FILES['updf']
        Uexcel_file = request.FILES['uexcel']
        Uimage      = request.FILES['uimage']

        udata.Cname       = Uname
        udata.Cgender     = Ugender
        udata.Cpdf_file   = Updf_file
        udata.Cexcel_file = Uexcel_file
        udata.Cimage      = Uimage

        udata.save()
        messages.success(request,"Successfully Upoladed")
        return redirect("dis_view")
    return render(request,"Upload_app/3update.html",{'udata':udata})


def Lets_delete(request,cid):
    del_data = Candidate_Profile.objects.get(id=cid)
    del_data.delete()
    messages.success(request,"Successfully Delete")
    return redirect("dis_view")