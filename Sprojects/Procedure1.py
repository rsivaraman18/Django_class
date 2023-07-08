1.Creation Of Django Project
command: django-admin startproject travel

2.Change Directory to Project
command: cd Budgetpredictor

3.Create New Application
command: python manage.py startapp mytrip

4.Add your application in settings.py File
Location: settings.py --> INSTALLED_APPS = [ 'APPLicationName']
Example : settings.py --> INSTALLED_APPS = [ 'mytrip']

5.Create Templates Folder & link in settings.py
Location: Project--> Create templates Folder --> APP FOLDER --> Required HTML FILES
link in : settings.py --> Template Location
command: import os
        mytemp = os.path.join(BASE_DIR,"templates")
        TEMPLATES = [{'DIRS':mytemp}]
    OR  TEMPLATES = [{'DIRS':"D:/visual studio Projects/Django-class2/travel/templates"}]



6.Create Static folder & link in settings.py
Location: Project--> Create static Folder --> css & JS & images FOLDER --> Required  FILES
mystatic = os.path.join(BASE_DIR,"static")
STATICFILES_DIRS = [mystatic]

7.Run server (To check Basic requirement are done without error)
python manage.py runserver 
look at: 127.0.0.1.8000s

8.Prepare Html File
{% block content %}
{% endblock %}
{% load static %}

9.views.py

def index(request):
    return render(request,"mytrip/home.html")

def result(request):
    utrain = request.GET['train']
    ufood  = request.GET['food']
    ubus   = request.GET['bus']
    ujeep  = request.GET['jeep']
    uhotel = request.GET['hotel']
    expense = int(utrain) + int(ufood) + int(ubus) + int(ujeep) + int(uhotel)
    oexpense = expense*15
    cdata  = {'one':expense , 'total':oexpense}
    return render(request,"Mytrip/budget.html",context=cdata)

10.urls.py

from mytrip import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('finalreport',views.result),
]

11.buget.html

    <link rel="stylesheet" href="../../static/css/mystyle.css">
<div class="container">
        <h2>Expense for 1 person : {{one}}</h2>
        <h2>Overall Expense : {{total}}</h2>
</div>

12.home.html
<div class="container">
        {% block content %}
        <form action="finalreport" autocomplete="off" >
            <table>
                <tr>
                    <th>Expense Table </th>
                </tr>
                <tr>
                    <th>Train</th>
                    <td><input type="text" name="train" id=""></td>
                </tr>
                <tr>
                    <th>Food</th>
                    <td><input type="text" name="food" id=""></td>
                </tr>
                <tr>
                    <th>Bus</th>
                    <td><input type="text" name="bus" id=""></td>
                </tr>
                <tr>
                    <th>Jeep</th>
                    <td><input type="text" name="jeep" id=""></td>
                </tr>
                <tr>
                    <th>Hotel</th>
                    <td><input type="text" name="hotel" id=""></td>
                </tr>
                <tr>
                    <td><input type="submit" value="submit"></td>
                </tr>
               
            </table>
        </form>
        {% endblock %}
    </div>












 
