from rest_framework import serializers
from .models import Movie

class MovieSerializer(serializers.Serializer):
    id = serializers.SerializerMethodField()
    title = serializers.CharField(max_length=100)
    description = serializers.CharField(max_length=100)
    active = serializers.BooleanField(default=True)

    def get_id(self, obj):
        return str(obj.id)

    def create(self, validated_data):
        movie = Movie(**validated_data)
        movie.save()
        return movie

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance

