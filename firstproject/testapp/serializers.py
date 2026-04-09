from rest_framework import serializers
from django.utils import timezone

from .models import Todo
class TodoSerializer(serializers.Serializer):
        id = serializers.SerializerMethodField()
        title = serializers.CharField()
        description = serializers.CharField()
        status = serializers.CharField()
        priority = serializers.CharField()
        due_date = serializers.DateTimeField(default=timezone.now(),required=False)
        created_at = serializers.DateTimeField(default=timezone.now(),required=False)
        modified_at = serializers.DateTimeField(default=timezone.now(),required=False)

        def validate_status(self, value):
            if value not in ['pending', 'in progress', 'completed']:
                raise serializers.ValidationError("Status must be 'pending', 'in progress', or 'completed'.")
            return value

        def validate_priority(self, value):
            if value not in ['low', 'medium', 'high']:
                raise serializers.ValidationError("Priority must be 'low', 'medium', or 'high'.")
            return value

        # def validate_due_date(self,value):
        #     if value < timezone.now():
        #         raise serializers.ValidationError("Due date cannot be in the past.")
        #     return value


        def get_id(self, obj):
            return str(obj.id)

        def create(self, validated_data):
            now = timezone.now()
            validated_data.setdefault('created_at', now)
            validated_data.setdefault('modified_at', now)
            todo = Todo(**validated_data)
            todo.save()
            return todo

        def update(self, instance, validated_data):
            for attr, value in validated_data.items():
                setattr(instance, attr, value)
            instance.modified_at = timezone.now()
            instance.save()
            return instance
