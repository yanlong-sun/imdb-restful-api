from rest_framework.serializers import ModelSerializer
from browser.models import TitleBasics, TitleAkas, TitleRatings, TitleEpisode
from browser.models import NameBasics, TitleCrew, TitlePrincipals


class TitleBasicsSerializer(ModelSerializer):
    class Meta:
        model = TitleBasics
        exclude = ['index']


class TitlePrincipalsSerializer(ModelSerializer):
    class Meta:
        model = TitlePrincipals
        exclude = ['index']


class TitleCrewSerializer(ModelSerializer):
    class Meta:
        model = TitleCrew
        fields = '__all__'


class TitleAkasSerializer(ModelSerializer):
    class Meta:
        model = TitleAkas
        exclude = ['index']


class TitleRatingsSerializer(ModelSerializer):
    class Meta:
        model = TitleRatings
        exclude = ['index']


class TitleEpisodeSerializer(ModelSerializer):
    class Meta:
        model = TitleEpisode
        exclude = ['index']


class NameBasicsSerializer(ModelSerializer):
    class Meta:
        model = NameBasics
        fields = '__all__'
