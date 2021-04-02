# Django Blog

### This project can be viewed [here](https://djangoblog0.pythonanywhere.com/)




* Blog website made using **Django** and deployed on **PythonAnywhere**. Uses **sqlite3** as database

* Profile images are compressed using [**Pillow**](https://pypi.org/project/Pillow/) before saving to db

* Website is HTTPS secured

### Features:

Users can:-

:white_check_mark: Register new account, login to existing one

:white_check_mark: Create, update, delete posts

:white_check_mark: Request password reset email

:white_check_mark: Change account username, email, password

:white_check_mark: Choose a custom profile picture

:white_check_mark: View posts by individual user



### Setup:

Always recommended to create a virtual environment

* Create a virtual environment named myenv
```python3 -m venv ./myenv```

* Activate it
```source myenv/bin/activate```

* Enter the virtual environment and then
```pip install -r requirements.txt```

## To run server

```python manage.py runserver```

## To make migrations

```python manage.py makemigrations```

## To see equivalent sql command for creating a migrations

```python manage.py sqlmigrate blog 0001```

## To launch shell

```python manage.py shell```

```from django.contrib.auth.models import User```

* To see all users

```User.objects.all()```

* To see first/last user

```User.objects.first() or .last()```

* To filter by username

```User.objects.filter(username='testuser')```

* for first result

```User.objects.filter(username='testuser').first()```

* To get info about a user

```user = User.objects.filter(username='testuser').first()```

- to get user id
```user.id```

- to get primary key for user(here same as id)
```user.pk```

* To get user using id

```User.objects.get(id=1)```

* To see all posts

```Post.objects.all()```

* To create a new post
```post_1=Post(title='Blog 1', content='First post!', author=user)```

* To save the post to our db
```post_1.save()```

* Save it to a variable post
```post = Post.objects.first()```

* Now to see it's content
```post.content```

* To see date_posted
```post.date_posted```

* To see post author
```post.author```

* To see post author email
```post.author.email```

* To see all posts by a user
```user.post_set```
```user.post_set.all()```

* To create a new post for a user
```user.post_set.create(title='Blog 3', content='Third Post')```

## To create users app
```python manage.py startapp users```


### Acknowledgments:

Inspired by [Corey M Schafer's](https://www.youtube.com/channel/UCCezIgC97PvUuR4_gbFUs5g) Django [Tutorial](https://www.youtube.com/playlist?list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p)
