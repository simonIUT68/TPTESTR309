reply = "hello"
        server_socket = socket.socket()
        port = self.text2.text()
        port = int(port)
        server_socket.bind((self.text1.text(), port))
        server_socket.listen(1)
        nom = f"Serveur en écoute sur le port : {port} ... "
        self.txt_mess.setText(nom)
        
        conn, address = server_socket.accept()
        nom = (f"Connexion acceptée de {port}")
        self.lab_mess.setText(nom)
        
        message = conn.recv(1024).decode()
        print(f"Message reçu: {message}")
            
        if message.lower() == "arret":
            conn.send("Serveur arrêté.".encode())
            conn.close()
            server_socket.close()
            print("Fermeture du serveur...") 
        elif message.lower() == "bye":
            conn.send("Client déconnecté.".encode())
            conn.close()
            print(f"Client {address} déconnecté.")
        else:
            reply = f"Serveur: Bien reçu votre message '{message}'."
            conn.send(reply.encode())