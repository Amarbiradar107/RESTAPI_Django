from django.db import models
from mongoengine import Document, StringField, IntField, DateTimeField
from django.utils import timezone
# Create your models here.


class Todo(Document):
    title = StringField(required=True)
    description = StringField()
    status = StringField(choices=['pending','in progress', 'completed'], default='pending')
    priority = StringField(choices=['low', 'medium', 'high'], default='low')
    due_date = DateTimeField(default=timezone.now())
    created_at = DateTimeField(default=timezone.now())
    modified_at = DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title




