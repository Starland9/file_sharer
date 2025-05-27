# File Sharer

File Sharer est une application de transfert de fichiers simple et intuitive avec une interface graphique moderne. Elle permet de partager facilement des fichiers entre différents appareils sur un réseau local.

![File Sharer Screenshot](https://github.com/Starland9/file_sharer/raw/main/screenshot.png)

## 📋 Fonctionnalités

- Interface utilisateur graphique intuitive
- Transfert de fichiers sur réseau local
- Barre de progression en temps réel
- Support multi-plateforme (Windows, macOS, Linux)
- Binaires pré-compilés disponibles dans les [releases](https://github.com/Starland9/file_sharer/releases)
- Support des architectures x86_64 et arm64 (Apple Silicon)

## 🚀 Téléchargement

Téléchargez la dernière version pour votre système d'exploitation dans la section [Releases](https://github.com/Starland9/file_sharer/releases).

| Plateforme | Fichier |
|------------|---------|
| Windows | `FileSharer_Windows_x86_64.exe` |
| macOS (Intel) | `FileSharer_macOS_x86_64.dmg` |
| macOS (Apple Silicon) | `FileSharer_macOS_arm64.dmg` |
| macOS (Universel) | `FileSharer_macOS_Universal.dmg` |
| Linux | `FileSharer_Linux_x86_64` |

## 🛠 Installation manuelle

### Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Étapes d'installation

1. Clonez le dépôt :
   ```bash
   git clone https://github.com/Starland9/file_sharer.git
   cd file_sharer
   ```

2. Créez et activez un environnement virtuel (recommandé) :
   ```bash
   python -m venv venv
   source venv/bin/activate  # Sur Windows : venv\Scripts\activate
   ```

3. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

## 🖥 Utilisation

### Lancer l'application

```bash
python app/main.py
```

### Comment utiliser

1. **Démarrer un serveur** :
   - Entrez l'adresse IP de votre machine (ou laissez 0.0.0.0 pour toutes les interfaces)
   - Choisissez un port (par défaut : 5000)
   - Cliquez sur "Start Server"

2. **Envoyer un fichier** :
   - Entrez l'adresse IP et le port du serveur distant
   - Cliquez sur "Select File" pour choisir un fichier
   - Cliquez sur "Send File" pour lancer le transfert

## 🛠 Compilation

Si vous souhaitez compiler vous-même l'application :

### Sous Linux :
```bash
chmod +x build_linux.sh
./build_linux.sh
```

### Pour Windows (depuis Linux) :
```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed \
  --name "FileSharer" \
  --add-data "app/style:app/style" \
  --add-data "app/ui:app/ui" \
  --hidden-import="PySide6.QtXml" \
  app/main.py
```

### Pour macOS (via GitHub Actions) :

1. Poussez vos modifications sur GitHub
2. Allez dans l'onglet "Actions"
3. Sélectionnez le workflow "Build macOS App (Universal)"
4. Téléchargez les artefacts générés

## 🐛 Dépannage

- **Erreur de port déjà utilisé** : Assurez-vous qu'aucune autre instance du serveur ne tourne
- **Problèmes de connexion** : Vérifiez votre pare-feu et assurez-vous que les machines sont sur le même réseau
- **Fichier non trouvé** : Vérifiez que le chemin du fichier est correct et que vous avez les permissions nécessaires

## 🤝 Contribuer

Les contributions sont les bienvenues ! Voici comment contribuer :

1. Forkez le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. Committez vos modifications (`git commit -m 'Add some AmazingFeature'`)
4. Poussez vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrez une Pull Request

## 📝 Licence

Ce projet est sous licence MIT - voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🙏 Remerciements

- [PySide6](https://www.qt.io/qt-for-python) - Pour l'interface graphique
- [tqdm](https://github.com/tqdm/tqdm) - Pour les barres de progression
- [GitHub Actions](https://github.com/features/actions) - Pour l'intégration continue
