# 🚗 Projet Covoiturage

## Structure

- **backend/** : API Django (gestion des utilisateurs, trajets, réservations…)
- **web/** : Interface web en React (pour les conducteurs & passagers)
- **mobile/** : Application mobile Expo React Native

## Installation

### Backend

```bash
cd backend
pip install -r ../requirements.txt
python manage.py runserver
```

### Web

```bash
cd web
npm install
npm run dev
```

### Mobile

```bash
cd mobile
npx expo start
```
