from django.db import models

class Books_Note(models.Model):
    title = models.CharField(max_length=40 ,null=True, blank=True)
    content = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self) :
        return self.title
    