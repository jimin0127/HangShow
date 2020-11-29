from django.db import models
from django.contrib.auth.models import User

class Assignment(models.Model):
    title = models.CharField(max_length=30)
    subject = models.CharField(max_length=30)
    content = models.TextField()
    created = models.DateField()
    endline = models.DateField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return '{}:{}'.format(self.title,self.author)
