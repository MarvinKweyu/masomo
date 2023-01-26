<p align="center">
  <img src="https://res.cloudinary.com/dlxhllkxl/image/upload/v1674462719/Masomo_v6nnbu.png" alt="masomo" width=250>
  <h2 align="center">Masomo</h2>
  <p align="center">An e-learning platform. Organise modules, courses and subjects with dynamic content between video and text. </p>
</p>

## Table of Contents
- [Table of Contents](#table-of-contents)
- [Setting up masomo](#setting-up-masomo)
  - [Manual](#manual)
  - [Docker - it just works(WIP)](#docker---it-just-workswip)


## Setting up masomo

### Manual
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

### Docker - it just works(WIP)
**Basic requirements**
 - Docker