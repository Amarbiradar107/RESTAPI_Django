from django.db import models
from mongoengine import Document, StringField, IntField, DateTimeField, ReferenceField, CASCADE, ListField, \
    EmbeddedDocumentListField, EmbeddedDocument
from django.utils import timezone
from rest_framework_mongoengine.utils import RelationInfo


# from ..user_detail.models import user
# Create your models here.



class User(Document):
    name = StringField(required=True)
    email = StringField(required=True, unique=True)
    password = StringField(required=True)

    def __str__(self):
        return self.name

class Todo(Document):
    # users = user()
    title = StringField(required=True)
    description = StringField()
    status = StringField(choices=['pending','in progress', 'completed'], default='pending')
    priority = StringField(choices=['low', 'medium', 'high'], default='low')
    due_date = DateTimeField(default=timezone.now())
    created_at = DateTimeField(default=timezone.now())
    created_by = ListField(ReferenceField(User))
    modified_at = DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title




