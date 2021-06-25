from django.db import models


# Create your models here.
class TaskModel(models.Model):
    title = models.CharField(max_length=250)
    done = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

