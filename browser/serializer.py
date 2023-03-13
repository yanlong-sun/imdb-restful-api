from rest_framework import serializers
from browser.models import BasicInfo
"""
Serializers
"""
class MovieSerializers(serializers.Serializer):
    tconst = serializers.CharField(max_length=100, read_only=True)
    titletype = serializers.CharField(max_length=100)  # Field name made lowercase.
    primarytitle = serializers.CharField(max_length=100)  # Field name made lowercase.
    originaltitle = serializers.CharField(max_length=100)  # Field name made lowercase.
    isadult = serializers.BooleanField()  # Field name made lowercase.
    startyear = serializers.DateField()  # Field name made lowercase.
    endyear = serializers.DateField()  # Field name made lowercase.
    runtimeminutes = serializers.CharField(max_length=100)  # Field name made lowercase.
    genres = serializers.CharField(max_length=100)

    def create(self, validated_data):
        new_movie = BasicInfo.objects.create(**validated_data)
        return new_movie