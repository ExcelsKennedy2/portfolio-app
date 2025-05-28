from django.db import models
from ckeditor.fields import RichTextField

class About(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    nationality = models.CharField(max_length=100, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    position = models.CharField(max_length=100)
    description = RichTextField(blank=True, null=True)
    signature = models.ImageField(upload_to='signatures/', null=True, blank=True)
    resume = models.FileField(upload_to='resumes/')
    experience = models.IntegerField(default=0)
    project_success = models.IntegerField(default=0)
    rate = models.IntegerField(default=0)

    def __str__(self):
        return self.name

class Education(models.Model):
    institution = models.CharField(max_length=100)
    starting_date = models.CharField(max_length=4 ,null=True, blank=True)
    year_of_completion = models.CharField(max_length=4, null=True, blank=True)
    level_of_education = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return self.institution

class Skill(models.Model):
    name = models.CharField(max_length=100)
    rate = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.name

class Experience(models.Model):
    work_place = models.CharField(max_length=100, null=True, blank=True)
    start_date = models.CharField(max_length=4, null=True, blank=True)
    end_date = models.CharField(max_length=4, null=True, blank=True)
    title = models.CharField(max_length=100)
    content = RichTextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    def __str__(self) -> str:
        return self.name

from django.utils import timezone

class Project(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=100)
    source_code = models.URLField(max_length=500)
    view_project = models.URLField(max_length=500)
    description = RichTextField(blank=True, null=True)
    created = models.DateTimeField(default=timezone.now)  # Add this line

    class Meta:
        ordering = ['-created']  # Orders by newest first



    def __str__(self) -> str:
        return self.name

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    client_position = models.CharField(max_length=100)
    testimonial_name = models.CharField(max_length=100)
    client_image = models.ImageField(upload_to='testimonials/')
    description = RichTextField(blank=True, null=True)

class Service(models.Model):
    name = models.CharField(max_length=100)
    description = RichTextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = RichTextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.subject

class Link(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField(max_length=500)
    icon = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name