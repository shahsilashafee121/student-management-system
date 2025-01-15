from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse
from .models import User,Registration,Notapproval,Student, LeaveApplication
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    return render(request, 'index.html')

def loged(request):
    if request.method=='POST':
       un=request.POST["username"]
       up=request.POST["password"]
       x=authenticate(request,username=un,password=up)
       if x is not None and x.is_superuser==1:
           login(request,x)
           request.session['a_id']=x.id
           return redirect(admin)
       elif x is not None and x.usertype=='teacher':
           login(request,x)
           request.session['t_id']=x.id
           teacher=Registration.objects.get(user=x)
           return render(request,'teacher.html',{'data':teacher})
       elif x is not None and x.usertype=='student':
           login(request,x)
           request.session['s_id']=x.id
           std=Student.objects.get(user=x)
           return render(request,'student.html',{'data':std})
       else:
           return HttpResponse("Invalid username ")
           
    else:
        return render(request,'loging.html')

def admin(request):
    return render(request,'admin.html')

def reg(request):
    if request.method=='POST':
        fn=request.POST['fname']
        sn=request.POST['sname']
        un=request.POST['uname']
        ue=request.POST['uemail']
        ug=request.POST['ugender']
        up=request.POST['upassword']
        uc=request.POST['cpassword']
        if up==uc:
            x=User.objects.create_user(username=un,password=uc, usertype='teacher')
            y=Registration.objects.create(user=x,firstname=fn,secondname=sn,email=ue,gender=ug,password=up,cnpassword=uc)
            y.save()
            return redirect(view)
        
    else:
        return render(request,'register.html')
    
def view(request):
    x=Registration.objects.all()
    return render(request,'regviewtable.html',{'data':x})

def regedit(request,id):
    x=Registration.objects.get(id=id)
    return render(request,'regedit.html',{'data':x})

def regupdate(request,id):
    na=request.POST['fname']
    sna=request.POST['sname']
    un=request.POST['uname']
    ue=request.POST['uemail']
    up=request.POST['password']
    cnp=request.POST['cpassword']
    
    old_data=Registration.objects.get(id=id)
    old_data.firstname=na
    old_data.secondname=sna
    old_data.user.username=un
    old_data.email=ue
    old_data.user.set_password(up)
    old_data.cnpassword=cnp
    
    old_data.user.save()
    old_data.save()
    return redirect(view)

def regdelete(request,id):
    x=Registration.objects.get(id=id)
    x.user.delete()
    x.delete()
    return redirect(view)


 
def teacher(request):
    return render(request,'teacher.html')

@login_required   
def teacherview(request):
    x=request.session.get('t_id')
    teacher=Registration.objects.get(user=x)
    return render(request,'teacherview.html',{'data':teacher})


@login_required
def editteacher(request):
    return render(request,'editteacher.html')

def regstudent(request):
    if request.method=='POST':
        fn=request.POST['firstname']
        sn=request.POST['secondname']
        un=request.POST['username']
        ue=request.POST['email']
        ug=request.POST['gender']
        ua=request.POST['age']
        ud=request.POST['department']
        uph=request.POST['phoneno']
        up=request.POST['password']
        uc=request.POST['cnpassword']
        if up==uc:
            y=Notapproval.objects.create(firstname=fn,secondname=sn,username=un,email=ue,age=ua,department=ud, phoneno=uph,gender=ug,password=up,cnpassword=uc)
            y.save()
            return  HttpResponse("YOU ARE SUCCESFULLY REGISTERED..")
        
        else:
            return render(request,'register.html')
    else:
    
        return render(request,'studentregistr.html')

def studentapproval(request):
    x=Notapproval.objects.all()
    return render(request,'studentapproval.html',{'data':x})

def approve(request,id):
    x=Notapproval.objects.get(id=id)
    fn=x.firstname
    sn=x.secondname
    un=x.username
    ue=x.email
    ud=x.department
    ug=x.gender
    ua=x.age
    uph=x.phoneno
    up=x.password
    ucp=x.cnpassword
    
    z=User.objects.create_user(username=un,password=up,usertype='student')
    y=Student.objects.create(user=z,firstname=fn,secondname=sn,email=ue,department=ud,gender=ug,age=ua,phoneno=uph,cnpassword=ucp)
    y.save()
    x.delete()
    return HttpResponse('SUCCESS')

def studentreject(request,id):
    x=Notapproval.objects.get(id=id)
    x.delete()
    return redirect(studentapproval)

def studentview(request):
    x=Student.objects.all()
    return render(request,'studentview.html',{'data':x})

@login_required
def updateteacher(request,id):
    fn=request.POST['fname']
    sn=request.POST["sname"]
    un=request.POST["uname"]
    ue=request.POST["uemail"]
    ug=request.POST['ugender']
    up=request.POST["upassword"]
    uc=request.POST["cnpassword"]
    
    x=Registration.objects.get(id=id)
    x.firstname=fn
    x.secondname=sn
    x.user.username=un
    x.email=ue
    x.gender=ug
    x.user.set_password(up)
    x.cnpassword=uc
    
    x.user.save()
    x.save()
    return redirect(editteacher)


@login_required
def studentprofileview(request):
    x=request.session['s_id']
    stud=Student.objects.get(user=x)
    return render(request,'studentprofileview.html',{'data':stud})

@login_required
def student(request):
    x=request.session['s_id']
    stud=Student.objects.get(user=x)
    return render(request,'studenthome.html',{'data':stud})
@login_required
def studentprofileedit(request):
    x=request.session['s_id']
    stud=Student.objects.get(user=x)
    return render(request,'studentprofileedit.html',{'data':stud})
@login_required
def studentprofileupdate(request,id):
    fn=request.POST['fname']
    sn=request.POST["sname"]
    un=request.POST["uname"]
    ue=request.POST["uemail"]
    ud=request.POST["udepartment"]
    ug=request.POST["ugender"]
    ua=request.POST["age"]
   
    
    old_data=Student.objects.get(id=id)
    old_data.firstname=fn
    old_data.secondname=sn
    old_data.user.username=un
    old_data.email=ue
    old_data.department=ud
    old_data.gender=ug
    old_data.age=ua
   
        
    old_data.user.save()
    old_data.save()
    return HttpResponse('SUCCESS')


def studentteacherview(request):
    x=Registration.objects.all()
    return render(request,'studentteacherview.html',{'data':x})
def teacherstudentview(request):
    x=Student.objects.all()
    return render(request,'teacherstudentview.html',{'data':x})
@login_required
def applyleave(request):
    if request.method == "POST":
        reason = request.POST.get('reason')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        LeaveApplication.objects.create(
            student=request.user,
            reason=reason,
            start_date=start_date,
            end_date=end_date
        )
        return redirect('leavestatus')
    return render(request, 'leaveapply.html')
@login_required
def leavestatus(request):
    applications = LeaveApplication.objects.filter(student=request.user)
    return render(request, 'leavestatus.html',{'applications': applications})


def logouts(request):
    logout(request)
    return redirect(home)