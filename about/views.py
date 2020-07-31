from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
# Create your views here.
def home(request):
    date = dt.date.today()
    
    
    return render(request, 'home.html', {"date": date})

def convert_dates(dates):
    #Function that gets the weekday
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    #Return the actual day of the week
    day = days[day_number]
    return day