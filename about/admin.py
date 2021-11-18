from django.contrib import admin
from .models import Project,tags,Profile,Project_comment, platforms, collaborators, ProjectCollab
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal =('tags','platforms',)

class ProjectAdmin2(admin.ModelAdmin):
    filter_horizontal =('tags','platforms','collaborators',)

admin.site.register(Project,ProjectAdmin)
admin.site.register(tags)
admin.site.register(platforms)
admin.site.register(collaborators)
admin.site.register(ProjectCollab,ProjectAdmin2)
admin.site.register(Profile)
admin.site.register(Project_comment)
