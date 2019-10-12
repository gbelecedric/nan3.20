  
from rest_framework.routers import DefaultRouter
from .apiviews import *
from django.urls import path
from . import views

router = DefaultRouter()
router.register('pays', PaysViewSet, base_name='pays')
router.register('ville', VilleViewSet, base_name='ville')
router.register('commune', CommuneViewSet, base_name='commune')


urlpatterns = [
    path('', views.register, name='register'),
    path('postregister', views.registers, name='register'),

]
urlpatterns += router.urls