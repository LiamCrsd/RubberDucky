import os
import time
import random

file = "./data.txt"
dic = {}

with open(file, 'r') as f:
    for line in f:
        key, value = line.strip().split(':')
        dic[key.strip()] = value.strip()

if os.name == "nt":
  for i in range(int(dic["Nb_terminaux"])):
    os.system("start python sousvirusW.py")
    time.sleep(1)
else:
  for i in range(int(dic["Nb_terminaux"])):
    os.system("gnome-terminal -- python3 sousvirusU.py")
  os.system("gnome-terminal -- python3 popup.py")  
  os.system("gnome-terminal -- python3 compteur.py")
