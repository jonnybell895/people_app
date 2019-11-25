from rest_framework import serializers
from people.models import People


class PeopleSerializer(serializers.ModelSerializer):
    """
    People Serializer

    Maps fields from models.fields to serializer.fields
    for serialization/de-serialization using JSON
    """
    class Meta:
        model = People
        fields = '__all__'
