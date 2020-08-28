from django.contrib import admin
from .models import Project,tags, Profile
# Register your models here.

class ProjectAdmin(admin.ModelAdmin):
    filter_horizontal =('tags',)

admin.site.register(Project,ProjectAdmin)
admin.site.register(tags)
admin.site.register(Profile)
