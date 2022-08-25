from django.shortcuts import render
from insertrecord.models import insertdata
import pyodbc
from sqlite3 import Cursor

from insertrecord.models import insertdata 

# def homepage(request):
#     return render(request,"index.html")

def saverecords(request):
    conn = pyodbc.connect('Driver={Sql Server};'
                            'Server=DESKTOP-4U7BNOM\SQLEXPRESS;'
                            'Database=django_python;'
                            'Trusted_Connection=yes;')
    if request.method=="POST":
        if request.POST.get('stname') and request.POST.get('stemail') and request.POST.get('stmob'):
            insertstvalues=insertdata()
            insertstvalues.stname=request.POST.get('stname')
            insertstvalues.stemail = request.POST.get('stemail')
            insertstvalues.stmob = request.POST.get('stmob')
            Cursor = conn.cursor()
            Cursor.execute("insert into sttable values ('"+insertstvalues.stname+"','"+insertstvalues.stemail+"','"+insertstvalues.stmob+"')")
            Cursor.commit()
            return render(request, 'index.html')
    else:
            return render(request, 'index.html')