from django.urls import path
from browser import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('title', views.TitleBaiscsView, basename='title')
router.register('name', views.NameBasicsView, basename='name')

urlpatterns = [
    path('title/<slug:tconst>/cast', views.TitlePrincipalsView.as_view({'get': 'list',
                                                                        'post': 'create'})),
    path('title/<slug:tconst>/crew', views.TitlePrincipalsView.as_view({'get': 'list',
                                                                        'post': 'create'})),
    path('title/<slug:tconst>/episode', views.TitleEpisodeView.as_view({'get': 'list',
                                                                        'post': 'create'})),
    path('title/<slug:tconst>/ratings', views.TitleRatingsView.as_view({'get': 'list',
                                                                        'post': 'create'})),
]

urlpatterns += router.urls
