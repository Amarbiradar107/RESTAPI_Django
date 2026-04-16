from django.db import models

# Create your models here.

# users/models.py
from mongoengine import Document, StringField, EmailField

class User(Document):
    name = StringField()
    email = EmailField()
