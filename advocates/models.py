from django.db import models

# Create your models here.

SESSION_STATUSES = (
    ('a', 'Approved'),
    ('s', 'Submitted'),
    ('r', 'Rejected'),
    ('p','Progress'),
)
class Court(models.Model):
    name = models.CharField(max_length = 400,null=True)
    courttype = models.CharField(max_length = 50,null=True)
    def __str__(self):
        return self.name

class Track(models.Model):
    casetype = models.CharField(max_length = 50,null=True)
    description = models.TextField(max_length = 1000,null=True)
    def __str__(self):
        return self.casetype

class Session(models.Model):
    clientname = models.CharField(max_length = 100)
    mobile = models.CharField(max_length = 100)
    case_describe = models.TextField(max_length = 2000)
    track = models.CharField(max_length=200,null=True)
    court = models.CharField(max_length=200,null=True)
    status = models.CharField(max_length = 1, choices = SESSION_STATUSES)
    hearing_date = models.DateTimeField(blank=True,null=True)
    def __str__(self):
        return self.clientname




