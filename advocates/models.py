from django.db import models

# Create your models here.

class Court(models.Model):
    name = models.CharField(max_length = 400)
    courttype = models.CharField(max_length = 50)
    def __str__(self):
        return self.name

class Track(models.Model):
    casetype = models.CharField(max_length = 50)
    description = models.TextField(max_length = 1000)
    def __str__(self):
        return self.casetype

SESSION_STATUSES = (
    ('a', 'Approved'),
    ('s', 'Submitted'),
    ('r', 'Rejected'),
    ('p','Progress'),
)

class Session(models.Model):
    clientname = models.CharField(max_length = 100)
    mobile = models.IntegerField()
    case_describe = models.TextField(max_length = 2000)
    track = models.ForeignKey(Track)
    court = models.ForeignKey(Court)
    status = models.CharField(max_length = 1, choices = SESSION_STATUSES)
    hearing_date = models.DateTimeField(blank=True,null=True)
    def __str__(self):
        return self.clientname




