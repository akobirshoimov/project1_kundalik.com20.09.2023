from django.urls import path
from .views import ListAPIView,CreateAPIView,UpdateAPIView


urlpatterns = [
    path('create/',CreateAPIView.as_view()),
    path('update/<int:kundalik_id>/',UpdateAPIView.as_view()),
    path('all/',ListAPIView.as_view())
]