# Create your models here.
# orders/models.py
from mongoengine import Document, StringField, IntField, ReferenceField
# from ..firstproject.userinfo.models.py import User   # ✅ Import from another app
from userinfo.models import User

class Order(Document):
    user = ReferenceField(User)   # Relationship
    product = StringField()
    amount = IntField()


