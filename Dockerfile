
# 1. Image de base avec Python 3.13
FROM python:3.13-slim

# 2. Répertoire de travail
WORKDIR /app

# 3. Copier les dépendances
COPY requirements.txt .

# 4. Installer les dépendances dans le conteneur
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copier le code source
COPY . .

# 6. Exposer le port de l'application
EXPOSE 8000

# 7. Démarrer FastAPI
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
