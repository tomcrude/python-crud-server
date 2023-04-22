from django.db import models
from django.contrib.auth.models import User

class Reviews(models.Model):
    title = models.CharField(max_length=30, null=False)
    description = models.CharField(max_length=100, null=False)
    img = models.ImageField(upload_to='images')
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.title
