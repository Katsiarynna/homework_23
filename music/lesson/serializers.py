from rest_framework import serializers
from .models import Music
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser


class MusicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Music
        fields = "__all__"


new_lesson = {"name": "violin", "description": "romantic instrument for you and job in orchestra", "teacher": "Vivaldi", "price": 50}
