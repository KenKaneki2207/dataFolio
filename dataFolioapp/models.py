from django.db import models
from django.contrib import admin

# Create your models here.
class Projects(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    img = models.ImageField(upload_to='static/projects/')
    skills = models.CharField(max_length=200)
    github_link = models.URLField(blank=True, null=True)
    website_link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.email}"
    
admin.site.register(Projects)
admin.site.register(Contact)