from django.urls import path

from .views import DataTable
from .csv import data_csv

app_name = 'datahub'
urlpatterns = [
    path('', DataTable.as_view(), name='datatable'),
    path('data_csv', data_csv, name='data_csv'),
]
