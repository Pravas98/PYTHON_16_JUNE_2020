from django.shortcuts import render, redirect
import requests
import sqlite3


def add_employee(request):
    if request.method == "POST":
        # process data
        name = request.POST['fullname']
        job  = request.POST['job']
        salary = request.POST['salary']

        with sqlite3.connect(r"c:\classroom\june16\hr.db") as con:
            cur = con.cursor()
            try:
                cur.execute("insert into employees(name,job,salary) values(?,?,?)",
                         (name, job, salary))
                con.commit()
                message = "Added Employee Successfully!"
                return render(request, 'add_employee.html', {'message' : message})
            except Exception as ex:
                print(ex)
                message = "Sorry! Could not add employee due to error!"
                return render(request, 'add_employee.html', {'message' : message})
    else:
        return render(request, 'add_employee.html')


def list_employees(request):
    con = sqlite3.connect(r"c:\classroom\june16\hr.db")
    cur = con.cursor()
    cur.execute("select * from employees")
    employees = cur.fetchall()
    con.close()
    return render(request, 'list_employees.html', {'employees': employees})
