from django.db import models

# Create your models here.
class BlogPost(models.Model):
	title = models.CharField(max_length = 200)
	image = models.FileField()
	body = models.TextField()