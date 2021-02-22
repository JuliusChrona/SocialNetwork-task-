# Social Network

## Start services

1. Clone repo
2. Create .env file
3. Run following command

```bash
python manage.py migrate
```

### .env file

```sh
SECRET_KEY = <DJANGO_SECRET_KEY>
HUNT_API_KEY = <hunter.io_API_KEY>
```

**SECRET_KEY** - Your secret key provided by Django.

**HUNT_API_KEY** - Api key provided by [hunter.io](hunter.io)

:warning:`Don't add your tokens in repository`

### Create super user

4. Create admin user

```bash
python manage.py createsuperuser
```

5. Run the server

```bash
python manage.py runserver
```

## Additional information

**Automated bot** implemented like django managment command.
Write next command to start it.
Config info lays in 'bot_config.json'

```bash
python manage.py activate_bot
```
