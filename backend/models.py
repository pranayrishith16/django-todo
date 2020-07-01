from django.db import models


class Todo(models.Model):
    text = models.CharField(max_length=400)

    def __str__(self):
        return self.text
