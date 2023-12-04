from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


# Create your models here.
class UserManager(BaseUserManager):
    # creation d'utilisateur simple 
    def create_user(self, profil, username,first_name,last_name,phone,address,password=None):
            if not username:
                raise ValueError("le nom d'utilisateur est obligatoire")
            if not first_name:
                raise ValueError('votre prenom est obligatoire')
            if not last_name:
                raise ValueError('votre nom est obligatoire')
            if not phone:
                raise ValueError('votre numero de telephone  est obligatoire')
            if not address:
                raise ValueError('votre adresse est obligatoire')

            user = self.model(
                profil=profil,
                username=username,
                first_name=first_name,
                last_name=last_name,
                phone=phone,
                address=address,
            )

            user.set_password(password)
            user.save(using=self._db)
            return user
    
    # cretion du super utilisateur admin
    def create_user(self, profil, username,first_name,last_name,phone,address,password):
            
            user = self.create_user(
                profil, username,first_name,last_name,phone,address,
                password=password,
               )
            user.is_admin = True
            user.save(using=self._db)
            return user

class User(AbstractBaseUser):
    profil= models.ImageField( upload_to='images/' ,blank=True)
    username = models.CharField(verbose_name="nom d'utilisateur")
    first_name=models.CharField(max_length=50, verbose_name='prenpm')
    last_name=models.CharField(max_length=50, verbose_name='nom')
    phone=models.CharField(max_length=20)
    address=models.CharField(max_length=50)
    is_active=models.BooleanField(default=False)
    is_admin =models.BooleanField(default=False)

    def set_profil(self,profil):
        self.profil=profil
    def set_first_name(self,first_name):
        self.first_name=first_name
    def set_last_name(self,last_name):
        self.last_name=last_name
    def set_phone(self,phone):
        self.phone=phone
    def set_address(self,address):
        self.profil=address
    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS =[first_name,last_name,phone,address]

    def __str__(self):
        return self.username
    
    def has_perm(self):
     return True

    def has_module_perms(self):
        return True

    @property
    def is_staff(self):
        return self.is_admin
        

