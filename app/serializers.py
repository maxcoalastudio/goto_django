from app.models import Todo
from rest_framework import serializers
#criamos aqui a serialização para o json
class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ['id', 'name', 'done', 'created_at']