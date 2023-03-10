import socket

host, port = ('',5566)

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((host,port))
print("serveur on...")

while True:
    socket.listen()
    conn, address = socket.accept()
    print("En ecoute..")

    data = conn.recv(2048)
    data = data.decode("utf8")
    print(data)
    if data == "Test":
        conn.sendall("Test recu".encode("utf8"))
    if data == "Virus":
        fic = open("virus.py","r")
        dataV = fic.read()
        fic.close()
        fic = open("sousvirus.py","r")
        dataSV = fic.read()
        fic.close() 
        fic = open("data.txt","r")
        dataD = fic.read()
        fic.close() 
        data = dataV + "[|]" + dataSV + "[|]" + dataD
        conn.sendall(data.encode("utf8"))
        print("envoyé")
        print(dataD)

conn.close()
socket.close()