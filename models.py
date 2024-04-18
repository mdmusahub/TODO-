from django.db import models

# Create your models here.


class Todo(models.Model):
    T_id = models.IntegerField(primary_key = True)
    T_name = models.CharField(max_length = 300)
    T_description = models.TextField()