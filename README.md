# File Sharer

File Sharer est un utilitaire de transfert de fichiers qui permet d'envoyer des fichiers d'un client à un serveur sur un réseau. Ce projet utilise Python et offre une interface en ligne de commande pour une utilisation facile.

## Fonctionnalités

- Envoi de fichiers à un serveur via une connexion socket.
- Suivi de la progression de l'envoi de fichiers grâce à `tqdm`.
- Exécution du serveur et du client en parallèle.
- Interface en ligne de commande avec des sous-commandes pour envoyer des fichiers ou démarrer un serveur.

## Installation

1. Clonez le dépôt :
   ```bash
   git clone <URL_DU_DEPOT>
   cd file_sharer
   ```

2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## Utilisation

### Démarrer le serveur

Pour démarrer le serveur, utilisez la commande suivante :

```bash
python app/main.py serve --host <ADRESSE_IP> --port <PORT>
```

### Envoyer un fichier

Pour envoyer un fichier au serveur, utilisez la commande suivante :

```bash
python app/main.py send <ADRESSE_IP> <CHEMIN_VERS_LE_FICHIER>
```

## Exemples

- Démarrer le serveur sur le port 5000 :
  ```bash
  python app/main.py serve --port 5000
  ```

- Envoyer un fichier `test.txt` au serveur :
  ```bash
  python app/main.py send 127.0.0.1 test.txt
  ```

## Contribuer

Les contributions sont les bienvenues ! Veuillez soumettre une demande de tirage pour toute amélioration ou correction de bogue.

## License

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus d'informations.
