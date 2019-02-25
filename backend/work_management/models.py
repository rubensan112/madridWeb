from django.db import models

# Create your models here.

class WorkProgrammedORM(models.Model):
    name = models.CharField(max_length=70, blank=False)
    creationDate = models.DateTimeField(auto_now_add=True)
    ownerOfNet = models.CharField(max_length=500, blank=True)
    description = models.CharField(max_length=500, blank=True)
    actualStartTime = models.DateTimeField(auto_now_add=True)
    actualEndTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '#{0} - {1}'.format(self.id, self.name)
