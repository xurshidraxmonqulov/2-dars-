from django.urls import path
from .views import AuthorListCreateView


app_name = 'authors'

urlpatterns = [
    path('create/', AuthorListCreateView.as_view(), name='create'),

]