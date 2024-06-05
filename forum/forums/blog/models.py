from django.db import models

# Create your models here.

class Thought(models.Model):
    topic = models.TextField(max_length=50)
    desc = models.TextField(max_length=200)
    thought_id = models.AutoField(primary_key=True)
    date = models.DateField()
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)
    def __str__(self):
        return self.topic

