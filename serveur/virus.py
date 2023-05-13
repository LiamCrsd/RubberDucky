import os
import time
import random
import atexit

"""
Il s'agit du script principale du virus qui régit les autres parties
"""

def arreter_virus(): #On fait en sorte que si l'utilisateur parvient a comprendre qu'il s'agit de l'origine du virus et l'arrete alors on arrete le virus 
    dicc = {}
    file = "./data.txt"
    with open(file, 'r') as f:
      for line in f:
        key, value = line.strip().split(':')
        dicc[key.strip()] = value.strip()
    dicc["Virus_actif"] = "0"
    with open(file, 'w') as f:
      for key, value in dicc.items():
        f.write(f"{key} : {value}\n")

atexit.register(arreter_virus)


file = "./data.txt"
dic = {}

with open(file, 'r') as f:
    for line in f:
        key, value = line.strip().split(':')
        dic[key.strip()] = value.strip()

if os.name == "nt":
  while True:
    try:
      #Suite d'événement pour windows
      for i in range(int(dic["Nb_terminaux"])):
        os.system("start python sousvirusW.py")
      os.system("start python popup.py")  
      os.system("start python compteur.py")
      time.sleep(1000000)
    except Exception as e:
      print("Arret du virus")

else:
  try:
    #Suit d'événement pour linux (ou macos)
    for i in range(int(dic["Nb_terminaux"])):
      os.system("gnome-terminal -- python3 sousvirusU.py")
    os.system("gnome-terminal -- python3 popup.py")  
    os.system("gnome-terminal -- python3 compteur.py")
  except Exception as e:
     print("Arret du virus")