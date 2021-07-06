from django.shortcuts import render
from django.http import HttpResponse
import datetime as dt
from .models import Project, Profile

# Create your views here.
def home(request):
    date = dt.date.today()
    profile =  Profile.get_profile()
    projects = Project.get_projects()

    return render(request, 'home.html', {"date": date, "profile": profile, "projects":projects})

def convert_dates(dates):
    #Function that gets the weekday
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    #Return the actual day of the week
    day = days[day_number]
    return day

def projects(request):
    date = dt.date.today()
    projects = Project.get_projects()
    return render(request, 'projects.html', {"date": date, "projects": projects})

def search_results(request):

    if 'about' in request.GET and request.GET["about"]:
        search_term = request.GET.get("about")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message":message, "about": searched_projects})
    
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})
