from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class Pays(models.Model):
    nom = models.CharField(max_length=30)
    continent = models.CharField(max_length=30)
    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nom
    class Meta:
        verbose_name = 'Pays'
        verbose_name_plural = 'Pays'
    
class Ville(models.Model):
    nom = models.CharField(max_length=30)
    pays = models.ForeignKey(Pays,null=True, on_delete=models.CASCADE, related_name='pays_ville')    
    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nom
    class Meta:
        verbose_name = 'Ville'
        verbose_name_plural = 'Villes'
    
class Commune(models.Model):
    nom = models.CharField(max_length=30)
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE, null=True,related_name='commune_ville')
    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.nom
    class Meta:
        verbose_name = 'Commune'
        verbose_name_plural = 'Communes'

class Profile(models.Model):

    # Appel de user
        
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')  # 1 user <---> 1 profil
        
    # Champs suplementaires
    pays = models.ForeignKey(Pays, on_delete=models.CASCADE, related_name='pays_etudiant', blank=True, null=True)
    ville = models.ForeignKey(Ville, on_delete=models.CASCADE, related_name='ville_etudiant', blank=True, null=True)
    commune = models.ForeignKey(Commune, on_delete=models.CASCADE, related_name='commune_etudiant', blank=True, null=True)
    contacts = models.CharField(max_length=30)
    image = models.ImageField(upload_to='profile/', default='useravatar.png')
    birth_date = models.DateField(blank=True, null=True)
    statut = models.BooleanField(default=True)
    date_add = models.DateTimeField(auto_now_add=True)
    date_upd = models.DateTimeField(auto_now=True)

    # Initialisation a la creation
        
    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, created, **kwargs):
        instance.profile.save()
        
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'