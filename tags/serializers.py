# Stdlib imports
# Core Django imports
# Third-party app imports
from rest_framework import serializers
# Imports from your apps
from .models import Tag


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        exclude = ('id', 'timeStamp', )


class TagQueryResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('merchandiseID', )
