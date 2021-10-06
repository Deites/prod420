from django.urls import path

from .views import DataFromHubViewsets


app_name = 'restapi'
urlpatterns = [
    path('create/', DataFromHubViewsets.as_view({'post' : 'create'}), name='createdata'),
]