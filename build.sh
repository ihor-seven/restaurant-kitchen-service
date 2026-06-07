#!/bin/bash

echo "🔧 Installing dependencies..."
pip install -r requirements.txt

echo "📂 Applying migrations..."
python manage.py makemigrations
python manage.py migrate

echo "🎨 Collecting static files..."
python manage.py collectstatic --noinput

echo "👤 Creating superuser (skip if already exists)..."
# python manage.py createsuperuser

echo "🚀 Starting server..."
python manage.py runserver 0.0.0.0:8000
