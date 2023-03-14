from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import serializers
from browser.models import BasicInfo
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ViewSet, GenericViewSet
from rest_framework.viewsets import ModelViewSet
"""
Serializer
"""


class MovieSerializers(serializers.ModelSerializer):
    class Meta:
        model = BasicInfo
        fields = '__all__'


# class MovieSerializers(serializers.Serializer):
#     tconst = serializers.CharField(max_length=100, read_only=True)
#     # Field name made lowercase.
#     titletype = serializers.CharField(max_length=100)
#     # Field name made lowercase.
#     primarytitle = serializers.CharField(max_length=100)
#     # Field name made lowercase.
#     originaltitle = serializers.CharField(max_length=100)
#     isadult = serializers.BooleanField()  # Field name made lowercase.
#     startyear = serializers.DateField()  # Field name made lowercase.
#     endyear = serializers.DateField()  # Field name made lowercase.
#     runtimeminutes = serializers.CharField(max_length=100)
#     genres = serializers.CharField(max_length=100)

#     def create(self, validated_data):
#         new_movie = BasicInfo.objects.create(**validated_data)
#         return new_movie

#     def update(self, old_date, validated_data):
#         BasicInfo.objects.filter(
#             tconst=old_date.tconst).update(**validated_data)
#         updated_data = BasicInfo.objects.get(tconst=old_date.tconst)
#         return updated_data

"""
VIEWS
"""
# """
# BASED ON GenericViewSet
# """


class movieView(ModelViewSet):
    queryset = BasicInfo.objects.all()
    serializer_class = MovieSerializers
    lookup_field = 'tconst'


# # """
# # BASED ON ViewSet( new 'dispatch')
# # """


# class movieView(ViewSet, ListCreateAPIView, RetrieveUpdateDestroyAPIView):
#     queryset = BasicInfo.objects.all()
#     serializer_class = MovieSerializers
#     lookup_field = 'tconst'

#     def get_all(self, request):
#         return self.list(request)

#     def post(self, request):
#         return self.create(request)

#     def get_one(self, request, tconst):
#         return self.retrieve(request)

#     def put(self, request, tconst):
#         return self.update(request)

#     def delete(self, request, tconst):
#         return self.destroy(request)


# # """
# # BASED ON ListCreateAPIView, RetrieveUpdateDestroyAPIView
# # """


# class movieView(ListCreateAPIView):
#     queryset = BasicInfo.objects.all()
#     serializer_class = MovieSerializers


# class movieDetailView(RetrieveUpdateDestroyAPIView):
#     queryset = BasicInfo.objects.all()
#     serializer_class = MovieSerializers
#     lookup_field = 'tconst'


# # """
# # BASED ON Mixins
# # """


# class movieView(GenericAPIView, ListModelMixin, CreateModelMixin):
#     queryset = BasicInfo.objects.all()[:10]
#     serializer_class = MovieSerializers

#     def get(self, request):
#         return self.list(request)

#     def post(self, request):
#         return self.create(request)


# class movieDetailView(GenericAPIView, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
#     queryset = BasicInfo.objects.all()
#     serializer_class = MovieSerializers
#     lookup_field = 'tconst'

#     def get(self, request, tconst):
#         return self.retrieve(request)

#     def put(self, request, tconst):
#         return self.update(request)

#     def delete(self, request, tconst):
#         return self.destroy(request)


# # """
# # BASED ON GenericAPIView
# # """


# class movieView(GenericAPIView):
#     queryset = BasicInfo.objects.all()[:10]
#     serializer_class = MovieSerializers

#     def get(self, request):
#         serializer = self.get_serializer(
#             instance=self.get_queryset(), many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         # check if the data is valid
#         if serializer.is_valid():  # serializer.validate_date  serializer.errors
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)


# class movieDetailView(GenericAPIView):
#     queryset = BasicInfo.objects.all()
#     serializer_class = MovieSerializers
#     lookup_field = 'tconst'

#     def get(self, request, tconst):
#         serializer = self.get_serializer(
#             instance=self.get_object(), many=False)
#         return Response(serializer.data)

#     def put(self, request, tconst):
#         serializer = self.get_serializer(
#             instance=self.get_object(), data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.error)

#     def delete(self, reqiest, tconst):
#         self.get_object().delete()
#         return Response()

# """
# BASED ON APIVive
# """
# class movieView(APIView):
#     def get(self, request):
#         movie_list = BasicInfo.objects.all()[:10]
#         # Declaring serializers,
#         # 'instance' is used for serialize
#         # 'data' is used for deserialize
#         serializer = MovieSerializers(instance=movie_list, many=True)
#         return Response(serializer.data)

#     def post(self, request):
#         serializer = MovieSerializers(data=request.data)
#         # check if the data is valid
#         if serializer.is_valid():  # serializer.validate_date  serializer.errors
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# class movieDetailView(APIView):
#     def get(self, request, tconst):
#         movie = BasicInfo.objects.get(tconst=tconst)
#         serializer = MovieSerializers(instance=movie, many=False)
#         return Response(serializer.data)

#     def put(self, request, tconst):
#         update_movie = BasicInfo.objects.get(tconst=tconst)
#         serializer = MovieSerializers(instance=update_movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

#     def delete(self, request, tconst):
#         BasicInfo.objects.get(tconst=tconst).delete()
#         return Response()
