fichier = open("index.html","w")

fichier.write("<html><body><h1>Site web automatique</h1>")
fichier.write("<p>Ceci est le site du client <b>client1</b></p>")
fichier.write("<div><img src='https://media.istockphoto.com/id/1443562748/fr/photo/mignon-chat-gingembre.jpg?s=612x612&w=0&k=20&c=ygNVVnqLk9V8BWu4VQ0D21u7-daIyHUoyKlCcx3K1E8='>")
fichier.write("</body></html>")

fichier.close()
