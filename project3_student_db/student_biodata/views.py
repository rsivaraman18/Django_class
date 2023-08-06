from django.shortcuts import render

# Create your views here.
from . models import Student_info
def home(request):
    return render(request,'student_biodata/1home.html') 


def new_register(request):
    if request.method=='POST':
        Cname    = request.POST['cname']
        Cage     = request.POST['cage']
        Cgender  = request.POST['cgender']
        Caddress = request.POST['caddress']
        Cemail   = request.POST['cemail']

        obj = Student_info()

        obj.Name    = Cname
        obj.Age     = Cage
        obj.Gender  = Cgender
        obj.Address = Caddress
        obj.Email   = Cemail

        obj.save()
        
        print("Successfullly *** Data are inserted into database ***")
        return render(request,'student_biodata/2registration.html')
    return render (request,'student_biodata/2registration.html')

def view_all_datas(request):
    mydata = Student_info.objects.all()
    return render(request,'student_biodata/3viewall.html',{'cdata':mydata})

def view_one(request):
    if request.method=="POST":
        owndata = {'Name':'sivacheck','Age':55,'Gender':'Male','Address':"Ramanthapuram","Email":'sivaaas@gmail.com'}
        return render(request,'student_biodata/4view.html',{'onedata':owndata})
    return render(request,'student_biodata/4view.html')

