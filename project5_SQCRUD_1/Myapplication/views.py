from django.shortcuts import render,redirect
from datetime import date
from django.contrib import messages
from . models import Our_datas
# Create your views here.

def Registration(request):
    if request.method=="POST":
        try:
            name = request.POST['uname'].title()
            dob  = request.POST['udob']
            
            #dob = "2021-02-17"
            today  = date.today()
            dyear,dmonth,dday = dob.split('-')
            age = today.year - int(dyear) -((today.month, today.day) < (int(dmonth), int(dday)))  

            gender = request.POST['ugender']
            state = request.POST['ustate']
            contact = request.POST['ucontact']
            email = request.POST['uemail']
            print('Datas now',name,dob,age,gender,state,contact,email)
            
            #messages.success(request,"Successfully Collected")
            
            # To upload Datas into Database using Object
            myobject         = Our_datas()
            myobject.Name    = name
            myobject.Dob     = dob
            myobject.Age     = age
            myobject.Gender  = gender
            myobject.State   = state
            myobject.Email   = email
            myobject.Contact = contact
            # Save the data into dabase
            myobject.save()
        
            messages.success(request,"Successfully Uploadded")
            return render(request,'Myapplication/1register.html')

        except Exception as msg:
            messages.warning(request,msg)
            print('Sry !',msg)
            return render(request,'Myapplication/1register.html')        
    return render(request,'Myapplication/1register.html')


def view_all(request):
    collected_data = Our_datas.objects.all()

    if collected_data:
        prog_msg  = request.session.pop('prog_msg', None)
        if prog_msg != None:
            messages.success(request, prog_msg)
        else:
            msg = "Siva Welcomes You"
            messages.info(request,msg)
        return render(request,'Myapplication/2viewall.html',{"viewdata":collected_data}) 
    else:
        msg="Yet No Datas were Registered"
        return render(request,'Myapplication/2viewall.html')




def update_data(request,cid):
    c_udata = Our_datas.objects.get(id=cid)
    if request.method=="POST":
        try:
            name = request.POST['uname'].title()
            dob  = request.POST['udob']
            
            # To Calculate Age
            today  = date.today()
            dyear,dmonth,dday = dob.split('-')
            age    = today.year - int(dyear) -((today.month, today.day) < (int(dmonth), int(dday)))  

            gender   = request.POST['ugender']
            state    = request.POST['ustate']
            contact  = request.POST['ucontact']
            email    = request.POST['uemail']
            # To upload Datas into Database using Object
            
            c_udata.Name    = name
            c_udata.Dob     = dob
            c_udata.Age     = age
            c_udata.Gender  = gender
            c_udata.State   = state
            c_udata.Email   = email
            c_udata.Contact = contact
            # Save the data into dabase
            c_udata.save() 
            #messages.success(request,"Successfully Uploadded")
            request.session['prog_msg'] = "Data's are Uploaded Successfully"
            return redirect('allview')
            

        except Exception as msg:
            request.session['prog_msg'] = msg            
            return redirect("allview")
    
    return render(request,'Myapplication/3update.html',{"cudata":c_udata})


def delete_data(request,cid):
    try:
        del_data = Our_datas.objects.get(id=cid)    
        request.session['prog_msg'] = del_data.Name + " Deleted From Database" 
        del_data.delete()
    except Exception as msg:
        request.session['prog_msg']= msg
    return redirect("allview")
    
    



def ready_to_search(request):
    if request.method=="POST":
        search_term  = request.POST['searchme'].title()
        coll_sdata   = Our_datas.objects.filter(Name=search_term)
        return render(request,'Myapplication/2viewall.html',{"viewdata":coll_sdata})
    return redirect("allview")