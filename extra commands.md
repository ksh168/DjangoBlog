## To run server
python manage.py runserver

## To make migrations
python manage.py makemigrations

## To see equivalent sql command for creating a migrations
python manage.py sqlmigrate blog 0001

## To see all users
User.objects.all()

## To see first/last user
User.objects.first() or .last()

## To filter by username
User.objects.filter(username='testuser')

* for first result
User.objects.filter(username='testuser').first()

## To get info about a user
user = User.objects.filter(username='testuser').first()
* user id
user.id
* to get primary key for user(here same as id)
user.pk

## To get user using id
User.objects.get(id=1)

## To see all posts
Post.objects.all()

