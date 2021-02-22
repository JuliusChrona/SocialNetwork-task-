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
__SECRET_KEY__  - Your secret key provided by Django.

__HUNT_API_KEY__ - Api key provided by [hunter.io](hunter.io)

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
__Automated bot__ implemented like django managment command.
Write next command to start it.
```bash
python manage.py activate_bot
```