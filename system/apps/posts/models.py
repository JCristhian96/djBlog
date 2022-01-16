from re import S
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    order = models.IntegerField()
    created_at = models.DateTimeField(auto_created=True)
    
    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'