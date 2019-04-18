from django.db import models

# Create your models here.

class Problem(models.Model):
    pname=models.CharField(max_length=200)

    def __str__(self):
        return self.pname

class Option(models.Model):
    oname=models.CharField(max_length=100)
    oshu=models.IntegerField
    pid=models.ForeignKey('Problem',on_delete=models.CASCADE)

    def __str__(self):
        return self.oname
