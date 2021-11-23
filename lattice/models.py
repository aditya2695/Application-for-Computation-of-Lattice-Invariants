from django.db import models

# Create your models here.

class Lattice(models.Model):

    name = models.CharField(max_length=255)
    length_a = models.FloatField()
    length_b = models.FloatField()
    length_c = models.FloatField()
    angle_a = models.FloatField()
    angle_b = models.FloatField()
    angle_c = models.FloatField()
    image  =models.CharField(max_length=2500)

class LatticeTypes(models.Model):

    name = models.CharField(max_length=255)
    length_a = models.FloatField()
    length_b = models.FloatField()
    length_c = models.FloatField()
    angle_a = models.FloatField()
    angle_b = models.FloatField()
    angle_c = models.FloatField()
    image  =models.CharField(max_length=2500)
    bravais_types  =models.CharField(max_length=255)

class lattice_2D_data(models.Model):


    id = models.AutoField(primary_key=True)
    a = models.FloatField()
    b = models.FloatField()
    gamma = models.FloatField()


class lattice_3D_data(models.Model):

    identifier = models.CharField(max_length=6)
    a = models.FloatField()
    b = models.FloatField()
    c = models.FloatField()
    alpha = models.FloatField()
    beta = models.FloatField()
    gamma = models.FloatField()
    bravais_types  =models.CharField(max_length=255)

class latticeEntries():

    id = models.AutoField(primary_key=True)
    a = models.FloatField()
    b = models.FloatField()
    c = models.FloatField()
    alpha = models.FloatField()
    beta = models.FloatField()
    gamma = models.FloatField()
    bravais_types  =models.CharField(max_length=255)
    addedTime = models.DateTimeField(auto_now_add=True)
    
class UserFile(models.Model):

    timestamp = models.DateTimeField(auto_now_add=True)
    file = models.FileField(verbose_name="User image", upload_to="user_images")

class FileModel(models.Model):
    doc = models.FileField(upload_to='media/')


class FilesUpload(models.Model):

    file = models.FileField()
    
    