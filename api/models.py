from django.db import models

# Create your models here.


class Jobs(models.Model):
    title = models.CharField(max_length=200, null=True)
    Company = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=250, null=True)
    salary = models.IntegerField(null=True, blank=True)
    Contact = models.CharField(max_length=200, null=True)


def __str__(self):
    return self.title
