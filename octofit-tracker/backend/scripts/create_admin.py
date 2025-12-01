from django.contrib.auth import get_user_model
import os

User = get_user_model()
username = os.getenv('OCTA_ADMIN_USER', 'admin')
email = os.getenv('OCTA_ADMIN_EMAIL', 'admin@example.com')
pwd = os.getenv('OCTA_ADMIN_PW', 'adminpass')

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, pwd)
    print('Superuser created:', username)
else:
    print('Superuser exists:', username)
