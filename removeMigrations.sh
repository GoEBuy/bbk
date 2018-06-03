#1. clear db
#drop database dbname

#2. remove migrations
rm users/migrations/0*.py
rm users/migrations/0*.pyc

rm focus/migrations/0*.py
rm focus/migrations/0*.pyc

rm order/migrations/0*.py
rm order/migrations/0*.pyc

#3. create database
#python manage.py makemigrations [appnme]
#python manage.py makemigrations users
#python manage.py migrate [users]
