from __future__ import unicode_literals

from django.db import models

from mongoengine import *


# Create your models here.
class User(Document):
    email = EmailField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)