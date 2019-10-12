# Fonction qui genere le username


’’’python

import codecs
import uuid
import sys
def generateUsername(nom, preneom): 
    if not (len(nom) > 1 or len(prenom) > 1):
        print("Please input your full and last name.")
        sys.exit()
    first_letter_nom = nom[0][0]
    first_letter_prenom = prenom[0][0]
    key = uuid.uuid4().hex[:3].upper()
    code = first_letter_nom.upper() + first_letter_prenom.upper() + key
    code = codecs.encode(code, 'rot_13')
    username = ("Nan3.20_" + code)
    return(username)
’’’