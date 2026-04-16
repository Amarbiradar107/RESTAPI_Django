from django.db import models

# Create your models here.
from django.db import models
from mongoengine import Document, StringField
# Create your models here.

class user(Document):
    name = StringField(required=True)
    email = StringField(required=True)