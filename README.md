<p align="center">
  <img src="https://res.cloudinary.com/dlxhllkxl/image/upload/v1674462719/Masomo_v6nnbu.png" alt="masomo" width=250>
  <h2 align="center">Masomo</h2>
  <p align="center">An e-learning platform. Organise modules, courses and subjects with dynamic content between video and text. </p>
</p>

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Setting up masomo](#setting-up-masomo)
  - [Docker (Recommended)](#docker-recommended)
    - [Development Setup](#development-setup)
    - [Production Setup](#production-setup)
  - [Manual Setup](#manual-setup)


## Setting up masomo

### Docker (Recommended)
**Basic requirements**
- Docker
- Docker Compose

#### Development Setup

The development environment uses SQLite for the database and includes hot-reload functionality.

1. Copy the example environment file (optional):
```bash
cp .env.dev.example .env
```

2. Build and start the development containers:
```bash
docker-compose -f docker-compose.dev.yml up --build
```

2. Access the application at `http://localhost:8000`

3. Default superuser credentials (created automatically):
   - Username: `admin`
   - Password: `admin`
   - Email: `admin@masomo.com`

4. **Sample Data**: The development environment automatically populates the database with 5 Computer Science courses:
   - Full Stack Web Development with Django
   - Python for Data Science and Analytics
   - Machine Learning Fundamentals
   - Computer Networks and Security
   - Database Design and SQL

5. To run management commands:
```bash
docker-compose -f docker-compose.dev.yml exec web python manage.py <command>
```

6. To manually populate/re-populate sample courses:
```bash
docker-compose -f docker-compose.dev.yml exec web python manage.py populate_courses
```

7. To stop the containers:
```bash
docker-compose -f docker-compose.dev.yml down
```

#### Production Setup

The production environment uses PostgreSQL database and uWSGI server.

1. Create your environment file:
```bash
cp .env.example .env
```

2. Edit `.env` and update the following critical variables:
   - `SECRET_KEY`: Generate a secure random key
   - `DATABASE_PASSWORD`: Set a strong database password
   - `POSTGRES_PASSWORD`: Must match DATABASE_PASSWORD
   - `ALLOWED_HOSTS`: Set your domain names

3. Build and start the production containers:
```bash
docker-compose up --build -d
```

3. The application will be available at `http://localhost:8000`

4. To view logs:
```bash
docker-compose logs -f web
```

5. To run management commands:
```bash
docker-compose exec web python manage.py <command>
```

6. To create a superuser:
```bash
docker-compose exec web python manage.py createsuperuser
```

7. To stop the containers:
```bash
docker-compose down
```

8. To stop and remove all data (including database):
```bash
docker-compose down -v
```

**Production Notes:**
- Generate a secure `SECRET_KEY` (use Django's `get_random_secret_key()`)
- For production deployment, add a reverse proxy (nginx/traefik) in front of the application
- Consider using Docker secrets or a secrets management service for sensitive data

### Manual Setup
**Basic requirements**
- memcached


Install project python requirements and migrate the server
```bash
pip install -r requirements.txt
python manage.py migrate
```

Start memcache on a different terminal
```bash
memcached -l 127.0.0.1:11211
```

Run the project and access the components on `127.0.0.1:8000`
```bash
python manage.py runserver
```