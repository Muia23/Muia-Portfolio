from django.db import models
from django.db.models.aggregates import Count
from tinymce.models import HTMLField
from ckeditor.fields import RichTextField

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_tags(self):
        self.save()

    @classmethod
    def get_project_tags(cls, id):
        project = cls.objects.get(pk=id)
        return project


class platforms(models.Model):
    plat_name = models.CharField(max_length =100)
    plat_icon = models.URLField(max_length =500)
    plat_type = models.CharField(max_length =100)

    def __str__(self):
        return self.plat_name

    def save_tags(self):
        self.save()

    @classmethod
    def get_project_platforms(cls, id):
        platforms = cls.objects.get(pk=id)
        return platforms    

class collaborators(models.Model):
    name = models.CharField(max_length =30)
    github_link = models.URLField(max_length =500)

    def __str__(self):
        return self.name

    def save_tags(self):
        self.save()

    @classmethod
    def get_project_collaborators(cls, id):
        people = cls.objects.get(pk=id)
        return people

class Profile(models.Model):
    profile_name = models.CharField(max_length = 100)
    about = HTMLField()
    profile_image = models.URLField(max_length = 2000, blank=False)

    def __str__(self):
        return self.profile_name

    @classmethod
    def get_profile(cls):
        profile = cls.objects.first()
        return profile

class Project(models.Model):
    title = models.CharField(max_length= 60)
    description = RichTextField(blank = False)
    tags = models.ManyToManyField(tags)    
    platforms = models.ManyToManyField(platforms)    
    projectimage1 = models.URLField(max_length =500)
    projectimageurl1 = models.URLField(max_length =500)
    projectimage2 = models.URLField(max_length =500)
    projectimageurl2 = models.URLField(max_length =500)
    projectimage3 = models.URLField(max_length =500, blank=True, null=True)
    projectimageurl3 = models.URLField(max_length =500, blank=True, null=True)
    projectimage4 = models.URLField(max_length =500, blank=True, null=True)
    projectimageurl4 = models.URLField(max_length =500, blank=True, null=True)
    projectimage5 = models.URLField(max_length =500, blank=True, null=True)
    projectimageurl5 = models.URLField(max_length =500, blank=True, null=True)

    def __str__(self):
        return self.title

    @classmethod
    def get_projects(cls):
        projects = cls.objects.order_by('-id')
        return projects

    @classmethod
    def get_project_by_tags(cls, tag):
        projects = cls.objects.filter(tags = tag)
        return projects

    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains= search_term)
        return projects

    @classmethod
    def get_project_detail(cls, id):
        project = cls.objects.get(pk=id)
        return project

class Project_comment(models.Model):
    project = models.ForeignKey(Project, related_name="comments",on_delete=models.CASCADE, blank=False)
    name = models.CharField(max_length=255, blank=False)
    body = models.TextField(blank=False)
    date_added = models.DateTimeField(auto_now_add=True, blank=False)

    def __str__(self):
        return '%s - %s' % (self.project.title, self.name)

    class Metaa:
        ordering = ['-date_added']

def ready(self):

    Project.objects.annotate(
        comments_total=Count('Project_comment')
    )

class ProjectCollab(models.Model):
    title = models.CharField(max_length= 60)
    description = RichTextField(blank = False)
    projectimage = models.URLField(max_length =500)
    projectimageurl = models.URLField(max_length =500)
    tags = models.ManyToManyField(tags)    
    collaborators = models.ManyToManyField(collaborators)    
    platforms = models.ManyToManyField(platforms)        

    def __str__(self):
        return self.title

    @classmethod
    def get_projects(cls):
        projects = cls.objects.order_by('-id')
        return projects