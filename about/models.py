from django.db import models
from tinymce.models import HTMLField

# Create your models here.
class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

    def save_tags(self):
        self.save()

class Profile(models.Model):
    profile_name = models.CharField(max_length = 100)
    about = HTMLField()
    profile_image = models.ImageField(upload_to = 'images/')

    def __str__(self):
        return self.profile_name

    @classmethod
    def get_profile(cls):
        profile = cls.objects.first()
        return profile

class Project(models.Model):
    title = models.CharField(max_length= 60)
    description = HTMLField()
    tags = models.ManyToManyField(tags)
    project_image = models.ImageField(upload_to = 'images/')

    
    @classmethod
    def get_projects(cls):
        projects = cls.objects.order_by('-title')
        return projects

    @classmethod
    def get_project_by_tags(cls, tag):
        projects = cls.objects.filter(tags = tag)
        return projects

    @classmethod
    def search_by_title(cls,search_term):
        projects = cls.objects.filter(title__icontains= search_term)
        return projects