from django.db import models

# Create your models here.

from mongoengine import Document, StringField, IntField, BooleanField


class Movie(Document):
    title = StringField(required=True)
    description = StringField(required=True)
    active = BooleanField(default=True)

    def __str__(self):
        return self.title
