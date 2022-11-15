from django.db import models
from ckeditor.fields import RichTextField


class Team(models.Model):
    fullname = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    position = models.CharField(max_length=250, help_text='Position in the Company')
    brief_info = models.TextField(help_text='Brief Intro')
    date_joined = models.DateField()
    about = RichTextField()
    image = models.ImageField(upload_to='team')
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.fullname

    
class HomePage(models.Model):
    hero_title = models.CharField(max_length=100)
    hero_paragraph = models.CharField(max_length=250)
    hero_image = models.ImageField(upload_to='home')

    class Meta:
        verbose_name_plural = 'Home page'

    def __str__(self):
        return f'Home Page'


class Cause(models.Model):
    home = models.ForeignKey(HomePage, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    image = models.ImageField(upload_to='causes')

    def __str__(self):
        return self.content


class About(models.Model):
    image = models.ImageField(upload_to='about')
    content = RichTextField()

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return f'About the company'


class Work(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True, help_text='Optional')
    content = RichTextField()
    image = models.ImageField(upload_to='works')
