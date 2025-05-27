#!/bin/bash

# Activer l'environnement virtuel
source .venv/bin/activate

# Nettoyer les builds précédents
echo "Nettoyage des builds précédents..."
rm -rf build/
rm -rf dist/

# Créer l'exécutable avec PyInstaller
echo "Création de l'exécutable..."
pyinstaller file_sharer.spec --noconfirm

# Vérifier si la compilation a réussi
if [ $? -eq 0 ]; then
    # shellcheck disable=SC2028
    echo "\n✅ Compilation réussie !"
    echo "L'exécutable se trouve dans le dossier 'dist/file_sharer/'
"
    
    # Afficher la taille du dossier
    du -sh dist/file_sharer/
    
    # Lancer l'application pour tester
    # shellcheck disable=SC2028
    echo "\nPour lancer l'application :"
    echo "cd dist/file_sharer/ && ./file_sharer"
else
    # shellcheck disable=SC2028
    echo "\n❌ Erreur lors de la compilation"
    exit 1
fi
