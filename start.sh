PORT=8000

if [[ $# -ge 1 ]];then
	echo "args: $@"
	PORT=$1
fi

echo "PORT: $PORT"

#python manage.py runserver 0:8000
python manage.py runserver 0:${PORT}
