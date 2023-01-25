from django.urls import re_path
from . import views

urlpatterns=[
    re_path(r'^$',views.home,name = 'home'),
    re_path(r'^projects/$',views.projects,name = 'projects'),
    re_path(r'^search/', views.search_results, name= 'search_results'),
    re_path(r'^projects/details/(\d+)/$',views.project_detail,name='projectsdetail'),
    re_path(r'^projects/collaborations$',views.project_collab,name='projectcollabs'),
]

