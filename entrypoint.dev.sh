#!/bin/bash

# Wait for memcached to be ready
echo "Waiting for memcached..."
while ! nc -z memcached 11211; do
  sleep 0.1
done
echo "Memcached started"

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate --noinput

# Create superuser if it doesn't exist
echo "Creating superuser if needed..."
python manage.py shell << END
from django.contrib.auth import get_user_model
User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@masomo.com', 'admin')
    print('Superuser created.')
else:
    print('Superuser already exists.')
END

# Start server
exec "$@"
