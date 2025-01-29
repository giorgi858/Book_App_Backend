from rest_framework.serializers import ModelSerializer
from .models import Books_Note

class Books_noteSerializer(ModelSerializer):
    class Meta:
        model = Books_Note
        fields = '__all__'