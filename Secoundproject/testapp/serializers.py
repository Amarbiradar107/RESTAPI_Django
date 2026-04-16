from rest_framework import serializers
from .models import watchlist,streamplatform

from django.core.serializers import serialize


class watchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model=watchlist
        fields='__all__'

    def create(self, validated_data):
        return watchlist.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)
        instance.description=validated_data.get('description',instance.description)
        instance.save()
        return instance



class streamingplatformSerializer(serializers.ModelSerializer):
    class Meta:
        model=streamplatform
        fields='__all__'





