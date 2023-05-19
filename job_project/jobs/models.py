from django.db import models

class User(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField(max_length=30)
    password = models.CharField(max_length=20)

    def __str__(self):
        return self.username


