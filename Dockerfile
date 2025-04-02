# Utiliser une image légère de Python
FROM python:3.10-slim

# Définir le répertoire de travail
WORKDIR /app

# Installer les dépendances système nécessaires
RUN apt-get update && apt-get install -y --no-install-recommends \
    && rm -rf /var/lib/apt/lists/*

# Copier uniquement les fichiers nécessaires pour installer les dépendances
COPY requirements.txt ./

# Installer les dépendances Python
RUN pip install --no-cache-dir -r requirements.txt

# Copier le reste du projet
COPY . .

# Executer les migrations
RUN python manage.py migrate

# Collecter les fichiers statiques
RUN python manage.py collectstatic --noinput

# Exposer le port 8000
EXPOSE 8000

# Lancer Django avec le serveur de production Gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "cloudintegration.wsgi:application"]
