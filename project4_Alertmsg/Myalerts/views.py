from django.shortcuts import render
from django.contrib import messages 
# Create your views here.
def msg_page(request):
    return render(request,'home.html')

def success_msg(request):
    messages.success(request,'This is a success message !')
    return render(request,'home.html')

def info_msg(request):
    messages.info(request,'This is a Info message !')
    return render(request,'home.html')

def warning_msg(request):
    messages.warning(request,'This is a Warning message !')
    return render(request,'home.html')

def danger_msg(request):
    messages.error(request,'This is a Danger/Error message !')
    return render(request,'home.html')
