from django.db import models

# Create your models here.

class serv(models.Model):
    servname = models.CharField(max_length=16)
    servdesc = models.TextField()
    servcost = models.IntegerField(default= 0)
    servpic = models.ImageField(upload_to = 'assets/images/productimg')
    servishigh = models.BooleanField(default=False)


class cust(models.Model):
    custfname = models.CharField(max_length=16)
    custlname = models.CharField(max_length=16)
    custemail = models.CharField(max_length=32)
    custphn = models.CharField(max_length=12)
    custpwd = models.CharField(max_length=16)
    custadd1 = models.CharField(max_length=64)
    custadd2 = models.CharField(max_length=64)
    custcity = models.CharField(max_length=16)
    custdist = models.CharField(max_length=16)
    custstate = models.CharField(max_length=16)
    custpincode = models.CharField(max_length=7)


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

class msg(models.Model):
    mname = models.CharField(max_length=16)
    memail = models.CharField(max_length=32)
    mphone = models.CharField(max_length=10)
    mmsg = models.TextField()

class clin(models.Model):
    cname = models.CharField(max_length=16)
    cimg = models.ImageField(upload_to = 'assets/images/clientimg')
    cliishigh = models.BooleanField(default=False)
    clinurl = models.CharField(max_length=64)


