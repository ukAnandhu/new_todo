from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=200)
    date = models.DateField()
    updated_at = models.DateTimeField(auto_now=True)
    priority = models.IntegerField()
    def __str__(self):
        return self.name
