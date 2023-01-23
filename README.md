# masomo
>An e-learning platform. Organise modules, courses and subjects with dynamic content between video and text. 

## Setting up masomo

## Manual
Clone the repo, install dependencies and run migrations.

```bash
pip install -r requirements.txt
python manage.py migrate
```

Start memecache on a different terminal
```bash
memecache -l 127.0.0.1:11211
```

Run the project and access the components on `127.0.0.1:8000`
```bash
python manage.py runserver
```

## Docker - it just works(WIP)
**Basic requirements**
 - Docker