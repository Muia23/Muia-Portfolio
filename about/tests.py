from django.test import TestCase
from models import Project, tags
# Create your tests here.

class ProjectTestCase(TestCase):

    def setUp(self):
        #creating a new tag
        self.new_tag = tags(name= 'Tester')
        self.new_tag.save()

        self.new_project= Project(title ='Test title of project', description='Just a test')
        self.new_project.save()

        self.new_project.tags.add(self.new_tag)

    #Testing instance
    def tearDown(self):
        tags.objects.all().delete()
        Project.objects.all().delete()



