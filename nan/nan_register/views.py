from django.shortcuts import render
from django.http import JsonResponse
import json
from .models import *

# Create your views here.
def register(request):
    templates_name = 'pages/register.html'
    data = {}
    return render(request,templates_name,data)

def registers(request):
    nom = request.POST.get('nom')
    prenom = request.POST.get('prenoms')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    password = request.POST.get('password')
    passwordconf = request.POST.get('passwordconf')
    pays = request.POST.get('pays')
    ville = request.POST.get('ville')
    commune = request.POST.get('commune')
    select = request.POST.get('select')
    naissance = request.POST.get('naissance')
    pay = Pays.objects.filter(nom=pays)
    vil = Ville.objects.filter(nom=ville)
    com = Commune.objects.filter(nom=commune)

    
    text = 'admin'
    
    print(pays,ville)
    try:
        if (nom is not None) and (prenom is not None) and (email is not None) and (phone is not None) and (password is not None) and (passwordconf is not None) and (select is not None):
            image = request.FILES['file']
            user = User(username= text, first_name = nom, last_name = prenom, email = email)
            user.save()
            
            user.profile.phone = phone
            user.profile.image = image
            user.profile.pays = pay
            user.profile.ville = vil
            user.profile.commune = com
            user.profile.genre = select
            user.profile.birth_date = naissance
            user.save()
            
            user.password = password
            user.set_password(user.password)
            user.save()
    except:
        pass
    datas = {
        'succes': True,
    }
    return JsonResponse(datas, safe=False)
