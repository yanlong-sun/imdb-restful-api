from django.http import Http404
from browser import serializers
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from browser.models import TitleBasics, NameBasics


class TitleBaiscsView(ModelViewSet):
    """
    router : api/titles/<title_id>
    """
    queryset = TitleBasics.objects.all()
    serializer_class = serializers.TitleBasicsSerializer
    lookup_field = 'tconst'


class TitlePrincipalsView(ModelViewSet):
    """
    router : api/titles/<title_id>/cast
    """
    serializer_class = serializers.TitlePrincipalsSerializer
    lookup_field = 'tconst'

    def get_queryset(self):
        title_tconst = self.kwargs['tconst']
        return TitleBasics.objects.get(tconst=title_tconst).principals


class TitleCrewView(ModelViewSet):
    """
    router: api/titles/<title_id>/crew
    """
    serializer_class = serializers.TitleCrewSerializer
    lookup_field = 'tconst'

    def get_queryset(self):
        title_tconst = self.kwargs['tconst']
        title_object = TitleBasics.objects.get(tconst=title_tconst)
        try:
            crews = title_object.crew
        except crews.DoesNotExist:
            raise Http404('Miss crew data')
        return crews


class TitleEpisodeView(ModelViewSet):
    """
    router: api/titles/<title_id>/episode
    """
    serializer_class = serializers.TitleEpisodeSerializer
    lookup_field = 'tconst'

    def get_queryset(self):
        title_tconst = self.kwargs['tconst']
        title_object = TitleBasics.objects.get(tconst=title_tconst)
        try:
            episodes = title_object.episode
        except episodes.DoesNotExist:
            raise Http404('Miss episode data')
        return [episodes]


class TitleRatingsView(ModelViewSet):
    """
    router: api/titles/<title_id>/ratings
    """
    serializer_class = serializers.TitleRatingsSerializer
    lookup_field = 'tconst'

    def get_queryset(self):
        title_tconst = self.kwargs['tconst']
        title_object = TitleBasics.objects.get(tconst=title_tconst)
        try:
            ratings = title_object.rating
        except ratings.DoesNotExist:
            raise Http404('Miss rating data')
        return [ratings]


class NameBasicsView(ModelViewSet):
    """
    router: api/name/<name_id>
    """
    queryset = NameBasics.objects.all()
    serializer_class = serializers.NameBasicsSerializer
    lookup_field = 'nconst'


"""
one more for :
api/people/<person_id>/titles: Get the titles a specific person is known for


"""
