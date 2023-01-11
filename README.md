# masomo
An e-learning platform

Install dependencies and run migrations.

```bash
pip install -r requirements.txt
python manage.py migrate
```

Start memecache on a different terminal
```bash
memecache -l 127.0.0.1:11211
```

Run the project and access the componentson `127.0.0.1:8000`
```bash
python manage.py runserver
```