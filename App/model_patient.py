from enum import Enum
from random import choice
from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Patient(BaseModel):
    nom : str
    prenom : str
    ssn : int

    def decrypter_ssn(self) -> List[List[str]]:
        
        ssn_digits = str(self.ssn)
        
        if ssn_digits[0] == "1" : 
            sexe = "Homme"
        else :
            sexe = "femme"
        # sexe = "Homme" if ssn_digits[0] == 1 else "Femme"
        annee_naissance = int(ssn_digits[1:3])
        mois_naissance = int(ssn_digits[3:5])
        departement_naissance = ssn_digits[5:7]
        pays_naissance = ssn_digits[7:10]
        indice_naissance = ssn_digits[10:13]
        cle_controle = int(ssn_digits[13:15])
        num_sans_cle = int(ssn_digits[:13])
        cle_attendue = 97 - (num_sans_cle % 97)
        cle_valide = cle_controle == cle_attendue
        
        return [
            [sexe],
            [str(annee_naissance)],
            [str(mois_naissance)],
            [departement_naissance],
            [pays_naissance],
            [indice_naissance],
            [str(cle_controle)],
            [cle_valide]
        ]


if __name__ == "__main__":
    patient = Patient(nom="Doe", prenom="John", ssn="1123456789012" + str(97 - (int("1123456789012") % 97))) #ICI testé avec une clef toujours valide
    print(patient)
    print(patient.decrypter_ssn())


