from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$',views.home,name = 'home'),
    url(r'^projects/$',views.projects,name = 'projects'),
    url(r'^search/', views.search_results, name= 'search_results'),
    url(r'^projects/details/(\d+)/$',views.project_detail,name='projectsdetail'),
    url(r'^projects/collaborations$',views.project_collab,name='projectcollabs'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
