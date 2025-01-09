from django.shortcuts import render, HttpResponse
from .models import Employee, Role, Department
from datetime import datetime
from django.db.models import Q
# Create your views here.
def index(request):
    return render(request, 'index.html')


def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request, 'view_all_emp.html',context)


def delete_emp(request, emp_id=0):
    if emp_id:
        try:
            emp_to_be_remove = Employee.objects.get(id=emp_id)
            emp_to_be_remove.delete()
            return HttpResponse('The selected employee has been Deleted')
        except:
            return HttpResponse('Please Enter a valid Employee ID')
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }

    return render(request, 'delete_emp.html', context)


def add_emp(request):

    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        salary = request.POST['salary']
        bonus = int(request.POST['bonus'])
        phone = int(request.POST['phone'])
        dept = int(request.POST['dept'])
        role = int(request.POST['role'])
        new_emp = Employee(firstname = firstname, lastname=lastname, salary=salary, bonus=bonus, dept_id=dept, role_id=role, phone=phone, hire_date = datetime.now()  )
        new_emp.save()
        return HttpResponse('Employee is added Successfully')
    elif request.method=='GET':
        return render(request, 'add_emp.html')
    else:
        print('get')
        return HttpResponse('An Exception has Occur')


def filter_emp(request):
    if request.method == 'POST':
        name = request.POST['name']
        dept = request.POST['dept']
        role = request.POST['role']
        emps = Employee.objects.all()
        if name:
            emps = emps.filter(Q(firstname__icontains = name) | Q(lastname__icontains = name ))
        if dept:
            emps = emps.filer(dept__name = dept)
        if role:
            emps = emps.filter(role__name = role)

        context = {
            'emps': emps
        }
        return render(request, 'view_all_emp.html', context)

    elif request.method =='Get':
        return render(request, 'filter_emp.html')
    else:
        return render(request, 'filter_emp.html')
