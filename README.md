## Django Migration
Migrate
```
python manage.py makemigrations
python manage.py migrate
```
Reset
```
python manage.py migrate --fake crowlizer_api zero
```

## DB Admin
Container up and see if it is up(healthy status means ready)
```
docker-compose up -d
docker ps
```
Container Login
```
docker exec -it crowlizer_admin_1 sh
```
if you want to see your database visually
https://stackoverflow.com/questions/58758377/how-to-fix-error-column-relhasoids-does-not-exist-in-phppgadmin
