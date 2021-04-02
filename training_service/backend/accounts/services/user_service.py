from django.contrib.auth.models import User


def create_user(username, email, first_name, last_name, password, groups):
    user = User(username=username, email=email, first_name=first_name, last_name=last_name)
    user.set_password(password)
    user.save()
    user.groups.set(groups)
    return user


def update_user(user, username=None, first_name=None, last_name=None, email=None, groups=None):
    if username:
        user.username = username
    if email:
        user.email = email
    if first_name:
        user.first_name = first_name
    if last_name:
        user.last_name = last_name
    user.save()
    if groups:
        user.groups.set(groups)
    return user
