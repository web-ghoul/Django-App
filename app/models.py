from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length = 1000,blank=True,null=True)
    def __str__(self):
        return self.title