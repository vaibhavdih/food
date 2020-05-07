from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Bookings
from datetime import datetime

@csrf_exempt
def show_index(request):
    if request.method=='GET':
        return render(request,'index.html')
    else:
        old_date=request.POST['date']
        pincode= request.POST['pincode']
        time = request.POST['time']
        datetimeobject = datetime.strptime(old_date, '%Y-%m-%d')
        newformat = datetimeobject.strftime('%d-%m-%Y')
        slots=Bookings.objects.filter(slot_date=newformat,pincode=pincode,slot_time=time)
        if len(slots)==0:
            key=0
        else:
            key =len(slots)



        return render(request,"cards.html",{'slots':slots,'date':newformat,'key':key,'pincode':pincode,'time':time})

@csrf_exempt
def register_booking(request):
    if request.method=='POST':
        date= request.POST['date']
        pincode = request.POST['pincode']
        time=request.POST['time']
        name=request.POST['name']
        contact=request.POST['contact']
        email=request.POST['email']
        units = request.POST['units']

        a=Bookings.objects.create(slot_date=date,slot_time=time,pincode=pincode,organisation_name=name,contact=contact,email_address=email,no_packets=units)
        slots = Bookings.objects.filter(slot_date=date, pincode=pincode, slot_time=time)
        if len(slots) == 0:
            key = 0
        else:
            key = len(slots)


        return render(request,"cards.html",{'slots':slots,'date':date,'key':key,'pincode':pincode,'time':time})



@csrf_exempt
def start_register(request):
    if request.method=='POST':
        date= request.POST['date']
        pincode = request.POST['pincode']
        time = request.POST['time']
        return render(request,"register.html",{"pincode":pincode,"date":date,"time":time})


