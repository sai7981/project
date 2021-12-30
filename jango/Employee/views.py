from django.shortcuts import render
from django.http import HttpResponse
from .models import Details
from django.contrib import messages

# Create your views here.

def empdetails(request):
   # return HttpResponse(' Hi this is my first app')

  return render(request, 'empdetails.html')

def Employee_1(request):
    try:
        print(request.POST)
        if request.method == 'POST':
            eno = request.POST['no']
            ename = request.POST['name']
            salary = request.POST['salary']
            emp=Details.objects.create( 
            emp_no=eno, emp_name=ename,salary=salary)
            emp.save()
        

            print(emp)

            print(eno, ename, salary)
    except Exception:
        messages.error(request, 'something went wrong')
        messages.info(request, 'it is looking like primary key issue')

    return render(request, 'empdetails.html') 

def fetchData(request):

  
    if request.method == 'GET':
        return render(request, 'empdetails.html')

    elif 'all' in request.POST:

        data = Details.objects.all()

        context = {
            'info': data
        }

        return render(request, 'empdetails.html', context)
    else:
        eno = request.POST['no']

        data = Details.objects.filter(emp_no=eno)

        context = {
            'info': data
        }

        print(context)
        return render(request, 'empdetails.html', context)

    