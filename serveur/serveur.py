import http.server
import socketserver

PORT = 8000 #On choisit le port sur lequel on lance le serveur qui represente un site web

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        try:
            #on définit une requete get tel que si l'url est un fichier que l'on peut télécharger alors on l'envoie
            #par exemple le fichier data.txt est présent dans le dossier il peut donc etre envoié
            #donc si l'on fait get http://localhost:8000/data.txt ce la envoir le fichier data.txt pour qu'il soit téléchargé (de meme avec une requete curl)
            filename = self.path[1:]
            with open(filename, 'rb') as file:
                self.send_response(200)
                self.send_header('Content-type', 'application/octet-stream')
                self.send_header('Content-Disposition', 'attachment; filename=' + filename)
                self.end_headers()
                self.wfile.write(file.read())
        except:
            #sinon on dit juste que l'addresse n'existe pas 
            super().do_GET()

with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
    #On lance ensuite le serveur dans une boucle infinie
    print("Serveur actif sur le port :", PORT)
    httpd.serve_forever()
