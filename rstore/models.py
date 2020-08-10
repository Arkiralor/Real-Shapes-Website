from django.db import models

# Create your models here.

class serv(models.Model):
    servname = models.CharField(max_length=16)
    servdesc = models.TextField()
    servcost = models.IntegerField(default= 0)
    servpic = models.ImageField(upload_to = 'assets/images/productimg')
    servishigh = models.BooleanField(default=False)


class users(models.Model):
    usrfname = models.CharField(max_length=16)
    usrlname = models.CharField(max_length=16)
    usremail = models.CharField(max_length=32)
    usrphn = models.CharField(max_length=12)
    usrpwd = models.CharField(max_length=16)
    usradd1 = models.CharField(max_length=64)
    usradd2 = models.CharField(max_length=64)
    usrcity = models.CharField(max_length=16)
    usrdist = models.CharField(max_length=16)
    usrstate = models.CharField(max_length=16)
    usrpincode = models.CharField(max_length=7)


class trans(models.Model):
    serv = models.IntegerField(default= 0)
    servname = models.CharField(max_length=16)
    servcost = models.IntegerField(default= 0)
    servqnt = models.IntegerField(default= 0)
    servtotal = models.IntegerField
    cust = models.IntegerField(default= 0)
    custname = models.CharField(max_length=16)


class cart(models.Model):
    serv = models.IntegerField(default= 0)
    servname = models.CharField(max_length=16)
    servcost = models.IntegerField(default= 0)
    servqnt = models.IntegerField(default= 0)
    servtotal = models.IntegerField(default= 0)
    cust = models.IntegerField(default= 0)
    custname = models.CharField(max_length=16)
