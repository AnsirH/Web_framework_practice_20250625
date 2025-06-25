from django.urls import path
from .views import index, detail_post

urlpatterns = [
    path('', index, name="index"),
    path('detail_post', detail_post, name="detail_post"),
]