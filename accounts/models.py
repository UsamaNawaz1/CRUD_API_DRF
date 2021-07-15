from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class post(models.Model):
    author = models.ForeignKey(User, related_name='related_author', on_delete=models.CASCADE)
    title = models.TextField()
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title