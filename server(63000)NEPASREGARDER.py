import socket
import threading


def gerer_client(connexion, adresse_client):
    print(f"Connexion établie avec {adresse_client}")

    while True:
        message_du_client = connexion.recv(1024).decode('utf-8')

        if message_du_client.upper() == 'FIN':
            print(f"Client {adresse_client} a fermé la connexion.")
            break

        print(f"De {adresse_client}: {message_du_client}")
        reponse_au_client = ("datasets : "
                             "make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)\n"
                             "train_test_split(X, y, test_size=0.2, random_state=42)\n"
                             "MLPClassifier(max_iter=1000, random_state=42)\n"
                             "accuracy_score() = GOOGLE\n")
        connexion.send(reponse_au_client.encode('utf-8'))

    # Fermer la connexion avec ce client
    connexion.close()


# Créer un socket
serveur_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Lier le socket à un port
host_name = ''
port_d_ecoute = 63000
serveur_socket.bind((host_name, port_d_ecoute))

# Mettre le socket d'écoute à l'état d'écoute
serveur_socket.listen()

print(f"Le serveur écoute sur le port {port_d_ecoute}...")

while True:
    # Accepter la connexion d'un client
    connexion_client, adresse_client = serveur_socket.accept()

    # Créer un nouveau thread pour gérer le client
    thread_client = threading.Thread(target=gerer_client, args=(connexion_client, adresse_client))
    thread_client.start()


