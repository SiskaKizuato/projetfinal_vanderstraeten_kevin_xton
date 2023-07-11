import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projet.settings')
django.setup()


from app.seed import run

if __name__== '__main__':
    run()
