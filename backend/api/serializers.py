from rest_framework.serializers import ModelSerializer
from .models import Books_Note
from django.contrib.auth.models import User

class Books_noteSerializer(ModelSerializer):
    class Meta:
        model = Books_Note
        fields = (
            'id',
            'content',
            'created',
            'updated',
            'author'
        )
        
        extra_kwargs = {"author": {"read_only": True}}
        
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        print(validated_data)
        user = User.objects.create_user(**validated_data)
        return user

        