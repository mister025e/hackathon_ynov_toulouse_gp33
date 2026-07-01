# 🚀 Interface Web - Assistant Financier (DEV WEB)

Bienvenue dans l'interface de discussion (chatbot) de notre assistant financier. Ce projet est réalisé avec **Streamlit** pour assurer un rendu fluide et rapide.

## 🛠️ Prérequis

Assurez-vous d'avoir installé **Python 3.8+** sur votre machine.

## 🕹️ Lancement Rapide (Recommandé)

Pour vous simplifier la vie, des scripts de lancement automatiques ont été créés. Ils vont installer les dépendances (si nécessaire) et démarrer l'application.

### Sur Windows
Double-cliquez simplement sur le fichier **`run.bat`** depuis l'explorateur de fichiers.
*(Ou lancez `.\run.bat` depuis votre terminal PowerShell/CMD).*

### Sur Linux / MacOS
Ouvrez votre terminal et exécutez le script Bash :
```bash
chmod +x run.sh  # (Optionnel, si les droits d'exécution manquent)
./run.sh
```

Une fois le script lancé, une page web s'ouvrira automatiquement dans votre navigateur par défaut à l'adresse **`http://localhost:8501`**.

---

## ⚙️ Lancement Manuel

Si vous préférez lancer le projet à la main, suivez ces étapes :

1. Ouvrez un terminal dans le dossier `rendu/devweb/`.
2. Installez les dépendances :
   ```bash
   pip install -r requirements.txt
   ```
3. Démarrez l'application Streamlit :
   ```bash
   streamlit run app.py
   # Ou selon votre environnement : python -m streamlit run app.py
   ```

## 🔌 Connexion au modèle IA

- **URL du serveur** : Par défaut, l'application pointe vers `http://localhost:11434` (Ollama). Vous pouvez changer cette adresse dynamiquement depuis le menu latéral de l'interface.
- **Mode hors-ligne** : Si l'équipe INFRA n'a pas encore déployé le modèle, l'interface continuera de fonctionner en simulant une réponse, ce qui vous permet de tester le visuel du chat sans être bloqué !
