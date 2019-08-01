from django.db import models

# Create your models here.


class Banks(models.Model):
    class Meta:
        db_table = 'banks'
    name = models.CharField(max_length=49)

    def __str__(self):
        return self.name


class Branches(models.Model):

    class Meta:
        db_table = 'branches'
    ifsc = models.CharField(max_length=11, primary_key=True, null=False)
    bank_id = models.ForeignKey(Banks, on_delete=models.CASCADE)
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)


class BankBranches(models.Model):

    class Meta:
        managed = False
        db_table = 'bank_branches'

    ifsc = models.CharField(max_length=11, primary_key=True, null=False)
    bank_id = models.ForeignKey(Banks, on_delete=models.CASCADE)
    branch = models.CharField(max_length=74)
    address = models.CharField(max_length=195)
    city = models.CharField(max_length=50)
    district = models.CharField(max_length=50)
    state = models.CharField(max_length=26)
    bank_name = models.CharField(max_length=49)

