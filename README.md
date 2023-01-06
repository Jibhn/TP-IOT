# TP-IOT

1er étape: installer l'environnement virtuel.

Pour ce faire, on va exécuter la commande suivante dans le terminal de l'ide : 
python -m venv venv

2eme étape : activer l'environnement virtuel.
voila la commande à exécuter sur le terminal :
.\venv\Scirpts\activate

Si vous avez une erreur à la suite de cette commande, ouvrez un powershell en tant qu'admin et taper cette commande :
Set-ExecutionPolicy Unrestricted
Une fois la commande executée taper "O" et faites entrer.


3eme étape : Créer un répertoire tp dans le dossier venv.
Se mettre sur le dossier venv : cd .\venv\ 
creer le dossier tp : mkdir tp
et se mettre sur le dossier tp: cd tp

4eme étape: installer flask et influxdb client.

Voici les commandes à taper:
- pip install flask
- pip install influxdb-client

Ne pas oublier de changer le nom du bucket, de l'orga, de l'username et de l'url dans le code du fichier app.py.

Pour lancer le projet se mettre sur le répaertoire tp dans un terminal et exécuter cette commande:
flask --app app run
