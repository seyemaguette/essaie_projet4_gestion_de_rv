from django.db import models

# Create your models here.
class Docteur(models.Model):
    photo_profil= models.ImageField(null=True, blank=True, upload_to='images/')
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    fontion = models.CharField(max_length=100)
    addresse = models.CharField(max_length=100)
    tel = models.CharField(max_length=50)
    email =models.EmailField()
    password = models.CharField(max_length=50)

    def  __str__(self):
        return f'{self.prenom} {self.nom}'\
    


class Patient (models.Model):
    prenom = models.CharField(max_length=100)
    nom = models.CharField(max_length=100)
    age = models.CharField(max_length=50)
    tel =models.CharField(max_length=50)
    adresse = models.CharField(max_length=100)

    def  __str__(self):
        return f'{self.prenom} {self.nom}'
    

class Rv(models.Model):
    titre = models.CharField(max_length=100)
    avec = models.CharField(max_length=50)
    date = models.DateField()
    heure = models.TimeField()
    lieu = models.CharField(max_length=50)


    def  __str__(self):
        return self.titre