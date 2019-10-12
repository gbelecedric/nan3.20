# vim: set fileencoding=utf-8 :
from django.contrib import admin

from . import models


class PaysAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'nom',
        'continent',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
        'id',
        'nom',
        'continent',
        'statut',
        'date_add',
        'date_upd',
    )


class VilleAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom', 'pays', 'statut', 'date_add', 'date_upd')
    list_filter = (
        'pays',
        'statut',
        'date_add',
        'date_upd',
        'id',
        'nom',
        'pays',
        'statut',
        'date_add',
        'date_upd',
    )


class CommuneAdmin(admin.ModelAdmin):

    list_display = ('id', 'nom', 'ville', 'statut', 'date_add', 'date_upd')
    list_filter = (
        'ville',
        'statut',
        'date_add',
        'date_upd',
        'id',
        'nom',
        'ville',
        'statut',
        'date_add',
        'date_upd',
    )


class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'user',
        'pays',
        'ville',
        'commune',
        'contacts',
        'genre',
        'image',
        'birth_date',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'user',
        'pays',
        'ville',
        'commune',
        'birth_date',
        'statut',
        'date_add',
        'date_upd',
        'id',
        'user',
        'pays',
        'ville',
        'commune',
        'contacts',
        'genre',
        'image',
        'birth_date',
        'statut',
        'date_add',
        'date_upd',
    )


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Pays, PaysAdmin)
_register(models.Ville, VilleAdmin)
_register(models.Commune, CommuneAdmin)
_register(models.Profile, ProfileAdmin)
