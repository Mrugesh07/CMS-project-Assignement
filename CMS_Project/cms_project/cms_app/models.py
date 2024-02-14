#

from django.core import validators

from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission


from django.db import models
from django.core import validators
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    phone = models.CharField(max_length=10, validators=[validators.RegexValidator(r'^\d{10}$')])
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    country = models.CharField(max_length=100, blank=True)
    pincode = models.CharField(max_length=6, validators=[validators.RegexValidator(r'^\d{6}$')])

    email = models.EmailField(unique=True, validators=[validators.EmailValidator(message='Please enter a valid email address.')])
    password = models.CharField(max_length=128, validators=[
        validators.MinLengthValidator(limit_value=8, message='Password must be at least 8 characters long.'),
        validators.RegexValidator(r'[A-Z]', message='Password must contain at least one uppercase letter.'),
        validators.RegexValidator(r'[a-z]', message='Password must contain at least one lowercase letter.'),
    ])
    first_name = models.CharField(max_length=30, validators=[validators.RegexValidator(r'^[A-Za-z ]+$', message='Please enter a valid first name.')])
    last_name = models.CharField(max_length=30, validators=[validators.RegexValidator(r'^[A-Za-z ]+$', message='Please enter a valid last name.')])

    groups = models.ManyToManyField(Group, related_name='user_set_custom', related_query_name='user_custom')
    user_permissions = models.ManyToManyField(Permission, related_name='user_set_custom',
                                              related_query_name='user_custom')

    def __str__(self):
        return self.username

class ContentItem(models.Model):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=300)
    summary = models.CharField(max_length=60)
    document = models.FileField(upload_to='documents/', validators=[validators.FileExtensionValidator(['pdf'], 'Only PDF files are allowed.')])
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='content_items', related_query_name='content_item')

    def __str__(self):
        return self.title