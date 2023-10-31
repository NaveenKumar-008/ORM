
# Create your models here.
from django.db import models
from django.contrib import admin
class Football (models.Model):
    pno=models.CharField(max_length=20,help_text="Player No.")
    name=models.CharField(max_length=100)
    team=models.CharField(max_length=100)
    age=models.IntegerField()
    position=models.CharField(max_length=100)

class FootballAdmin(admin.ModelAdmin):
    list_display=('pno','name','team','age','position')
