from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
import datetime as dt
from .models import Project, Profile, Project_comment, ProjectCollab
from .forms import CommentForm

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
    profile =  Profile.get_profile()
    projects = Project.get_projects()
    return render(request, 'projects.html', {"date": date, "profile": profile, "projects": projects})

def search_results(request):

    if 'about' in request.GET and request.GET["about"]:
        search_term = request.GET.get("about")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html', {"message":message, "about": searched_projects})
    
    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html', {"message": message})

def project_detail(request,id):
    profile =  Profile.get_profile()
    project =  Project.get_project_detail(id)
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)
        comment.project = project
        comment.save()     

        return HttpResponseRedirect(reverse('projectsdetail', args=[str(id)]))

    else:
        form = CommentForm()        

        return render(request, 'projectdetail.html',{"profile": profile, "project": project, "form":form})

def project_collab(request):
    profile =  Profile.get_profile()
    projects = ProjectCollab.get_projects()

    return render(request, 'projectcollab.html',{"profile": profile, "projects":projects})