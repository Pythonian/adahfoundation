from django.db import models


class Team(models.Model):
    fullname = models.CharField(max_length=250)
    position = models.CharField(max_length=250, help_text='Position in the Company')
    brief_info = models.TextField(help_text='Brief Intro')
    about = models.TextField()
    image = models.ImageField(upload_to='team')
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    linkedin = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.fullname