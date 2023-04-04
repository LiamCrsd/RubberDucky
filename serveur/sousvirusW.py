import os
import time
import random
try:
  fic = open("script2/data.txt","r")
except:
  fic = open("data.txt","r")
var = int((fic.readline())[14:])
fic.close()
count = 0
liste = ["chargement","tree"]
rand = random.choice(liste)
if rand == "chargement":
  while var:
    count +=1
    x = int((count/50)*40)
    try:
      fic = open("script2/data.txt","r")
    except:
      fic = open("data.txt","r")
    var = int((fic.readline())[14:])
    fic.close()
    print("Hack en cours " + "[" + "#"*x + "."*(40-x) + "]" )
    time.sleep(1)
  print("Echec du Hack")
elif rand == "tree":
  while var:
    try:
      fic = open("script2/data.txt","r")
    except:
      fic = open("data.txt","r")
    var = int((fic.readline())[14:])
    fic.close()
    os.system("tree")
    os.system("ipconfig")
  print("Echec du Hack")  