# vim: set fileencoding=utf-8 :
from django.contrib import admin
from django.utils.safestring import mark_safe
from . import models


class PaysAdmin(admin.ModelAdmin):

    list_display = (
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
    )


class VilleAdmin(admin.ModelAdmin):
    
    list_display = ('nom', 'pays', 'statut', 'date_add', 'date_upd')
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
    )


class CommuneAdmin(admin.ModelAdmin):
    
    list_display = ('nom', 'ville', 'statut', 'date_add', 'date_upd')
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
    )


class ProfileAdmin(admin.ModelAdmin):

    list_display = (
        'Photo',
        'user',
        'pays',
        'ville',
        'commune',
        'contacts',
        'birth_date',
        'statut',
        'date_add',
        'date_upd',
    )
    list_filter = (
        'statut',
        'date_add',
        'date_upd',
    )
    def Photo(self, obj):
        return mark_safe('<img src="{url}" width="100px" heigth="50px" />'.format(url=obj.image.url))


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Pays, PaysAdmin)
_register(models.Ville, VilleAdmin)
_register(models.Commune, CommuneAdmin)
_register(models.Profile, ProfileAdmin)
