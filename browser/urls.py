from django.urls import path
from browser import views
from rest_framework import routers
router = routers.DefaultRouter()
router.register('movie', views.movieView)
urlpatterns = [
    # path('', views.movieView.as_view({'get': 'list',
    #                                   'post': 'create'})),
    # path('<slug:tconst>/',
    #      views.movieView.as_view({'get': 'retrive',
    #                               'put': 'update',
    #                               'delete': 'destory'})),
]
urlpatterns += router.urls
