from django.shortcuts import render, HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from browser.models import BasicInfo
from browser.serializer import MovieSerializers

class movieView(APIView):
    def get(self, request):
        movie_list = BasicInfo.objects.all()[:10]
        # Declaring serializers, 
        # 'instance' is used for serialize
        # 'data' is used for deserialize
        serializer = MovieSerializers(instance=movie_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = MovieSerializers(data=request.data)
        # check if the data is valid
        if serializer.is_valid(): # serializer.validate_date  serializer.errors
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

class movieDetailView(APIView):
    def get(self, request, id):
        movie = BasicInfo.objects.get(tconst=id)
        serializer = MovieSerializers(instance=movie, many=False)
        return Response(serializer.data)


    def put(self, request, id):
        pass

    def delete(self, request, id):
        pass








"""
VIEWS
"""
# Create your views here.
# '''
# FBV
# '''
# def movie(request):
#     if request.method == 'GET':
#         return HttpResponse("GET...")
#     else:
#         return HttpResponse('POST...')

# '''
# CBV using View
# '''
# class movieView(View):
#     def get(self, request):
#         return HttpResponse("view GET...")
    
#     def post(self, request):
#         return HttpResponse("view POST...")
    
#     def delete(self, request):
#         return HttpResponse("view DELETE...")

# '''
# CBV using APIView
# '''
# class movieView(APIView):
#     def get(self, request):
#         return HttpResponse("view GET...")
    
#     def post(self, request):
#         return HttpResponse("view POST...")
    
#     def delete(self, request):
#         return HttpResponse("view DELETE...")

