# Generated by Django 3.1.3 on 2021-09-16 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_auto_20210916_1728'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='project_images',
            new_name='projectimages',
        ),
    ]
