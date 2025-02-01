from django.db import models

class Books_Note(models.Model):
    content = models.CharField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def __str__(self) :
        return self.content[0:50] 
    
