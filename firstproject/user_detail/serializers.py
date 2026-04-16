from rest_framework_mongoengine import serializers
from .models import user
class userserializer(serializers.DocumentSerializer):
    class Meta:
        model = user
        fields = '__all__'