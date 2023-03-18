from django.http import Http404
from browser import serializers
from browser import pagination
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ModelViewSet
from browser.models import TitleBasics, NameBasics
from browser.models import TitleEpisode, TitleRatings, TitleCrew, TitleAkas, TitlePrincipals


class TitleBasicsView(ModelViewSet):
    queryset = TitleBasics.objects.all()
    serializer_class = serializers.TitleBasicsSerializer
    lookup_field = 'tconst'

    pagination_class = pagination.BasicPagination

    def list(self, requst):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class TitleAkasView(ModelViewSet):
    serializer_class = serializers.TitleAkasSerializer
    lookup_field = 'titleid'
    pagination_class = pagination.BasicPagination

    def list(self, request, *args, **kwargs):
        title_tconst = self.kwargs['tconst']
        title_object = TitleBasics.objects.get(tconst=title_tconst)
        try:
            akas = title_object.akas.all()
        except TitleAkas.DoesNotExist:
            raise Http404('Miss alternate names data')
        queryset = self.filter_queryset(akas)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class TitlePrincipalsView(ModelViewSet):
    serializer_class = serializers.TitlePrincipalsSerializer
    lookup_field = 'tconst'
    pagination_class = pagination.BasicPagination

    def list(self, request, *args, **kwargs):
        title_tconst = self.kwargs['tconst']
        title_object = TitleBasics.objects.get(tconst=title_tconst)
        try:
            principals = title_object.principals.all()
        except TitlePrincipals.DoesNotExist:
            raise Http404('Miss casts data')
        queryset = self.filter_queryset(principals)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class TitleCrewView(ModelViewSet):
    serializer_class = serializers.TitleCrewSerializer
    lookup_field = 'tconst'

    def get_queryset(self):
        title_tconst = self.kwargs['tconst']
        title_object = TitleBasics.objects.get(tconst=title_tconst)
        try:
            crews = title_object.crew
        except TitleCrew.DoesNotExist:
            raise Http404('Miss crew data')
        return [crews]


class TitleEpisodeView(ModelViewSet):
    serializer_class = serializers.TitleEpisodeSerializer
    lookup_field = 'tconst'

    def get_queryset(self):
        title_tconst = self.kwargs['tconst']
        title_object = TitleBasics.objects.get(tconst=title_tconst)
        try:
            episodes = title_object.episode
        except TitleEpisode.DoesNotExist:
            raise Http404('Miss episode data')
        return [episodes]


class TitleRatingsView(ModelViewSet):
    serializer_class = serializers.TitleRatingsSerializer
    lookup_field = 'tconst'

    def get_queryset(self):
        title_tconst = self.kwargs['tconst']
        title_object = TitleBasics.objects.get(tconst=title_tconst)
        try:
            ratings = title_object.rating
        except TitleRatings.DoesNotExist:
            raise Http404('Miss rating data')
        return [ratings]


class NameBasicsView(ModelViewSet):
    queryset = NameBasics.objects.all()
    serializer_class = serializers.NameBasicsSerializer
    lookup_field = 'nconst'
    pagination_class = pagination.BasicPagination
