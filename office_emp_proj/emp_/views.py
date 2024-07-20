from .models import Employee,Role,Department
from datetime import datetime
from django.shortcuts import render,HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.db.models import Q


def index(request):
    return render(request,'index.html')

@csrf_protect
def viewemp(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    print(context)
    return render(request,'viewemp.html',context)

def addemp(request):
    #print("Hello in emp")
    
    if request.method=='POST':
        #print("POST")
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        phone=int(request.POST['phone'])
        dept=int(request.POST['dept'])
        role=int(request.POST['role'])
        print("Hello11")
        # location=request.POST['location']
        new_emp=Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,dept_id=dept,role_id=role,hire_date=datetime.now())
        print(new_emp)
        print("Hello11")
        new_emp.save()
        return HttpResponse('Employee Added successfully')  
    elif request.method=="GET":
        return render(request,'addemp.html')    
    else:
        #return HttpResponse('An error occured')
        return HttpResponse("Error occured")
    
def delemp(request,emp_id=0):
    if emp_id:
        try:
            id_to_remove=Employee.objects.get(id=emp_id)
            id_to_remove.delete()
            return HttpResponse("Deleted successfully")
        except:
            return HttpResponse("please select valid id")

    emps=Employee.objects.all()
    #print(emps)
    context={
        'emps':emps
    }
    return render(request,'delemp.html',context)


def editemp(request):
    if request.method=="POST":
        name=request.POST['name']
        dept=request.POST['dept']
        role=request.POST['role']
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains=name)|Q(last_name=name))
            
        if dept:
            emps=emps.filter(dept__name=dept)
        if role:
            emps=emps.filter(role__name=role)
        context={
            'emps':emps
        }
        
        
        return render(request,'viewemp.html',context)
    elif request.method=="GET":
        return render(request,'editemp.html')
    else:
        return HttpResponse("An error occured")

