from django import template
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import lecture,attendance_report,supportQueries,deployment_model
from django.contrib.auth.models import User
from datetime import datetime,timedelta,date
from django.utils import timezone
import json

@login_required(login_url="/login/")
def profile(request):
    
    u = request.user
    U = User.objects.get(id=u.id)
    projects = deployment_model.objects.filter(username=U).order_by('-date')[:3]
    context = {'segment': 'profile','projects':projects}
    return render(request,'home/profile.html',context)


@login_required(login_url="/login/")
def index(request):
    u = request.user
    U = User.objects.get(id=u.id)
    projects = deployment_model.objects.filter(username=U).order_by('-date')
    lecture_report = attendance_report.objects.filter(username=U,date__range=[timezone.now()-timedelta(days=30), timezone.now()])  
    lecture_reportvalue = {}
    for i in lecture_report:
        lecture_reportvalue[str(i.name)] = i.value

    lectures = list(lecture_reportvalue.keys())
    days = list(lecture_reportvalue.values()) 
    lectures = json.dumps(lectures)
    days = json.dumps(days)   

    U = User.objects.count()         # Total number of users
    # count = User.objects.filter(date_joined=datetime.today()).count()   Users Who Joined Today
    count = User.objects.filter(last_login__range=[timezone.now()-timedelta(days=1), timezone.now()]).count()  # Total number of active users today
    if count==0:
        count=1

    context = {'segment': 'index','projects':projects,'report':lectures,'days':days,'total_users':U,'todays_users':count}
    return render(request,'home/index.html',context)

@login_required(login_url="/login/")
def remove(request,pk):
    a = lecture.objects.get(pk=pk)
    a.delete()
    return redirect('lectures')


@login_required(login_url="/login/")
def lectures(request):
    u = request.user
    U = User.objects.get(id=u.id) 
    a = lecture.objects.filter(username=U)
    context = {'segment': 'lectures','a':a}

    resp = render(request,'features/lectures.html',context)
    return resp


@login_required(login_url="/login/")
def cd(request):
    context = {'segment': 'code_deployer','msg':''}

    if request.method=='POST':
        u = request.user
        U = User.objects.get(id=u.id)
        title = request.POST.get('title')
        link = request.POST.get('link')
        frontend = request.POST.get('Frontend')
        backend = request.POST.get('Backend')
        db = request.POST.get('Database')
        desc = request.POST.get('desc')
        deploy = deployment_model(project_name=title,desc=desc,username=U,backend_technology=backend,frontend_technology=frontend,
        database_used=db,link=link)
        deploy.save()
        context = {'segment': 'code_deployer','msg':'Your Code Will Be Deployed Soon'}

    resp = render(request,'features/code_deployer.html',context)
    return resp

@login_required(login_url="/login/")
def dspace(request):
    context = {'segment': 'dev_space'}
    resp = render(request,'features/dspace.html',context)
    return resp

@login_required(login_url="/login/")
def ml(request):
    context = {'segment': 'm_l'}
    resp = render(request,'features/ml.html',context)
    return resp    

@login_required(login_url="/login/")
def sp(request):
    context = {'segment': 's_p'}
    resp = render(request,'features/sp.html',context)
    return resp

@login_required(login_url="/login/")
def add_lecture(request):
    context = {'segment': 'lectures'}
    resp = render(request,'features/add_lecture.html',context)
    if request.method=='POST':
        sname = request.POST.get('sname')
        tname = request.POST.get('tname')
        link1 = request.POST.get('link')
        desc = request.POST.get('desc')
        u = request.user
        U = User.objects.get(id=u.id)

        new_lecture = lecture(name=sname,teacher_name=tname,desc=desc,link=link1,username=U)
        if new_lecture:
            new_lecture.save()           
            return redirect('lectures')    

    return resp    


@login_required(login_url="/login/")
def attendance(request,pk):
    b = lecture.objects.all()
    context = {'segment': 'lectures','a':b}
    resp = render(request,'features/lectures.html',context)
    if request.method=='POST':
        a = lecture.objects.get(pk=pk)    
        x = str(a.name)
        b = lecture.objects.all()
        context = {'segment': 'lectures','a':b}
        resp = redirect('lectures')
        c = x.replace(" ","")
        if request.COOKIES.get(c)=='1':
            msg = "You Have Already Put Your Attendance"
        else:
            if request.user.is_authenticated:
                u_n = request.user
                u = User.objects.get(id=u_n.id)
                try:
                    v = attendance_report.objects.get(name=a,username=u)
                    v.value = v.value + 1
                    v.date = datetime.now()
                    v.save()
                except Exception as e:
                    b = attendance_report(name=a,username=u,value=1,initial_date=datetime.now())
                    b.save()    

                msg = "You Have Put Your Attendance"
                resp.set_cookie(c,'1',max_age=1)

    return resp 

@login_required(login_url="/login/")
def about(request):
    context = {'segment':'about'}
    return render(request,'features/about.html',context)    


@login_required(login_url="/login/")
def support(request):
    if request.method=='POST':
        u = request.user
        U = User.objects.get(id=u.id)
        value = "Open"
        desc = request.POST.get('desc')
        typeq = request.POST.get('querytype')
        q = supportQueries(username=U,value=value,typeOfQuery=typeq,problemDesc=desc)
        q.save()
        msg = "You Have Submitted Your Response"
        context = {'segment':'support','msg':msg}
        return render(request,'features/support.html',context)
    context = {'segment':'support'}
    return render(request,'features/support.html',context)


def devs(request):
    context = {'segment':'developers'}
    return render(request,'features/devs.html',context)

def docs(request):
    context = {'context':'documentation'}
    return render(request,'features/docs.html',context)


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
