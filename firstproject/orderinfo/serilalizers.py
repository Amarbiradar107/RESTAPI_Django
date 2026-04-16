from rest_framework_mongoengine.serializers import DocumentSerializer
from .models import Order
from userinfo.models import User
from userinfo.serializers import UserSerializer


class OrderSerializer(DocumentSerializer):
    user = UserSerializer()  # Nested serializer for the user field
    class Meta:
        model = Order
        fields = '__all__'

        def create(self, validated_data):
            user_id = self.initial_data.get('user')
            user = User.objects.get(id=user_id)
            validated_data['user'] = user
            return super().create(validated_data)


