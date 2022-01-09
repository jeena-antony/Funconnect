from django.db.models import fields
from rest_framework import serializers
from .models import game

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = game
        fields = ['id','game_name','game_desc']