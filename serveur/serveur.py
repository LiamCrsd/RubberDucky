import http.server
import socketserver

PORT = 8000

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/data':
            filename = 'data.txt' # Remplacez 'nom_de_votre_fichier.ext' par le nom de votre fichier et son extension
            with open(filename, 'rb') as file:
                self.send_response(200)
                self.send_header('Content-type', 'application/octet-stream')
                self.send_header('Content-Disposition', 'attachment; filename=' + filename)
                self.end_headers()
                self.wfile.write(file.read())
        elif self.path == '/compteur':
            filename = 'compteur.py' # Remplacez 'nom_de_votre_fichier.ext' par le nom de votre fichier et son extension
            with open(filename, 'rb') as file:
                self.send_response(200)
                self.send_header('Content-type', 'application/octet-stream')
                self.send_header('Content-Disposition', 'attachment; filename=' + filename)
                self.end_headers()
                self.wfile.write(file.read())
        elif self.path == '/popup':
            filename = 'popup.py' # Remplacez 'nom_de_votre_fichier.ext' par le nom de votre fichier et son extension
            with open(filename, 'rb') as file:
                self.send_response(200)
                self.send_header('Content-type', 'application/octet-stream')
                self.send_header('Content-Disposition', 'attachment; filename=' + filename)
                self.end_headers()
                self.wfile.write(file.read())
        elif self.path == '/sousvirusU':
            filename = 'sousvirusU.py' # Remplacez 'nom_de_votre_fichier.ext' par le nom de votre fichier et son extension
            with open(filename, 'rb') as file:
                self.send_response(200)
                self.send_header('Content-type', 'application/octet-stream')
                self.send_header('Content-Disposition', 'attachment; filename=' + filename)
                self.end_headers()
                self.wfile.write(file.read())
        elif self.path == '/virus':
            filename = 'virus.py' # Remplacez 'nom_de_votre_fichier.ext' par le nom de votre fichier et son extension
            with open(filename, 'rb') as file:
                self.send_response(200)
                self.send_header('Content-type', 'application/octet-stream')
                self.send_header('Content-Disposition', 'attachment; filename=' + filename)
                self.end_headers()
                self.wfile.write(file.read())
        elif self.path == '/download':
            filename = 'download.py' # Remplacez 'nom_de_votre_fichier.ext' par le nom de votre fichier et son extension
            with open(filename, 'rb') as file:
                self.send_response(200)
                self.send_header('Content-type', 'application/octet-stream')
                self.send_header('Content-Disposition', 'attachment; filename=' + filename)
                self.end_headers()
                self.wfile.write(file.read())
        else:
            super().do_GET()

with socketserver.TCPServer(("", PORT), RequestHandler) as httpd:
    print("Serveur actif sur le port :", PORT)
    httpd.serve_forever()
