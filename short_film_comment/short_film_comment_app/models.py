from django.db import models

# Create your models here.
class Film(models.Model):
    id = models.IntegerField(primary_key=True)
    image_path = models.TextField()
    caption = models.TextField()
    information = models.TextField()
    information2 = models.TextField()
    introduction = models.TextField()

class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    film_id = models.IntegerField()
    content = models.TextField()