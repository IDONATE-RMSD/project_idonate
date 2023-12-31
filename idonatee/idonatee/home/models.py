from unittest.util import _MAX_LENGTH
from django.db import models
# from matplotlib import image



 
# Create your models here.
class Signupp(models.Model):
    username = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=10)
    role=models.CharField(max_length=10)
    
class Detail(models.Model):
    username=models.CharField(max_length=20)
    fullname=models.CharField(max_length=20)
    dob=models.DateField()
    email=models.EmailField()
    mobno=models.IntegerField()
    ge=models.CharField(max_length=10)
    age=models.IntegerField()
    bg=models.CharField(max_length=10)
    address=models.CharField(max_length=30)
    occupation=models.CharField(max_length=10)
    weight=models.IntegerField()
    height=models.IntegerField()
    an=models.CharField(max_length=10)
    tmr=models.CharField(max_length=10)
    ldd=models.DateField()
    dbo=models.CharField(max_length=10)
    image=models.ImageField(upload_to='pictures')

class Edit(models.Model):
    username=models.CharField(max_length=20)
    don_edit_email=models.EmailField()
    don_edit_mobno=models.IntegerField()
    don_edit_address=models.CharField(max_length=30)
    don_edit_occupation=models.CharField(max_length=10)
    don_edit_weight=models.IntegerField()
    don_edit_height=models.IntegerField()
    don_edit_an=models.CharField(max_length=10)
    don_edit_tmr=models.CharField(max_length=10)
    don_edit_ldd=models.DateField()
    don_edit_sid=models.CharField(max_length=10)
    don_edit_eidn=models.CharField(max_length=10)
    don_edit_dsbg=models.ImageField(upload_to='pictures')


class Rdetail(models.Model):
    username=models.CharField(max_length=20)
    fname=models.CharField(max_length=20)
    rdob=models.DateField()
    remail=models.EmailField()
    rmobno=models.IntegerField()
    rge=models.CharField(max_length=10)
    rage=models.IntegerField()
    rbg=models.CharField(max_length=10)
    raddress=models.CharField(max_length=30)
    roccupation=models.CharField(max_length=10)
    rweight=models.IntegerField()
    rheight=models.IntegerField()
    ran=models.CharField(max_length=10)
    rtmr=models.CharField(max_length=10)
    rlrd=models.DateField()
    rdbo=models.CharField(max_length=10)
    rimage=models.ImageField(upload_to='pictures')

class Odetail(models.Model):
    username=models.CharField(max_length=20)
    ofname=models.CharField(max_length=20)
    oemail=models.EmailField()
    omobno=models.IntegerField()
    oaddress=models.CharField(max_length=30)
    oimage=models.ImageField(upload_to='pictures')

class Odetail2(models.Model):
    username=models.CharField(max_length=20)
    olicenceid=models.CharField(max_length=20)
    oiimage=models.ImageField(upload_to='pictures')

class Hdetail(models.Model):
    username=models.CharField(max_length=20)
    hfname=models.CharField(max_length=20)
    hid=models.CharField(max_length=20)
    hemail=models.EmailField()
    hmobno=models.IntegerField()
    haddress=models.CharField(max_length=30)
    bbp=models.CharField(max_length=10)
    obp=models.CharField(max_length=10)
    himage=models.ImageField(upload_to='pictures')

class Hdetail2(models.Model):
    username=models.CharField(max_length=20)
    hlicenceid=models.CharField(max_length=20)
    hiimage=models.ImageField(upload_to='pictures')

class Detail2(models.Model):
    username=models.CharField(max_length=20)
    sid=models.CharField(max_length=10)
    eidn=models.IntegerField()
    dsbg=models.ImageField(upload_to='pictures')

class Rdetail2(models.Model):
    username=models.CharField(max_length=20)
    rsid=models.CharField(max_length=10)
    reidn=models.IntegerField()
    rdsbg=models.ImageField(upload_to='pictures')


class Quick(models.Model):
    
    qfname=models.CharField(max_length=20)
    qemail=models.EmailField()
    qmobno=models.IntegerField()
    qaddress=models.CharField(max_length=10)
    

class Recreq(models.Model):
    username=models.CharField(max_length=20)
    recusername=models.CharField(max_length=20)
    scor=models.CharField(max_length=20)

class Orgreq(models.Model):
    username=models.CharField(max_length=20)
    orgusername=models.CharField(max_length=20)
    orequest=models.CharField(max_length=20)

class Hosreq(models.Model):
    username=models.CharField(max_length=20)
    hosusername=models.CharField(max_length=20)
    requesth=models.CharField(max_length=20)

class Rhosreq(models.Model):
    username=models.CharField(max_length=20)
    rhosusername=models.CharField(max_length=20)
    hosuserreq=models.CharField(max_length=20)

class Rdonreq(models.Model):
    username=models.CharField(max_length=20)
    rdonusername=models.CharField(max_length=20)
    rec_req_to_donar=models.CharField(max_length=20)

class Rorgreq(models.Model):
    username=models.CharField(max_length=20)
    rorgusername=models.CharField(max_length=20)
    rec_req_to_organization=models.CharField(max_length=20)

class Odonreq(models.Model):
    username=models.CharField(max_length=20)
    odonusername=models.CharField(max_length=20)
    org_req_to_donar=models.CharField(max_length=20)

class Orecreq(models.Model):
    username=models.CharField(max_length=20)
    orecusername=models.CharField(max_length=20)
    Org_req_to_rec=models.CharField(max_length=20)

class Ohosreq(models.Model):
    username=models.CharField(max_length=20)
    ohosusername=models.CharField(max_length=20)
    org_req_to_hos=models.CharField(max_length=20)

class Hdonreq(models.Model):
    username=models.CharField(max_length=20)
    hdonusername=models.CharField(max_length=20)
    hospital_req_to_don=models.CharField(max_length=20)

class Hrecreq(models.Model):
    username=models.CharField(max_length=20)
    hrecusername=models.CharField(max_length=20)
    hsl_req_to_rec=models.CharField(max_length=20)

class Horgreq(models.Model):
    username=models.CharField(max_length=20)
    horgusername=models.CharField(max_length=20)
    hsl_req_to_organization=models.CharField(max_length=20)
