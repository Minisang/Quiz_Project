from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # /index 경로에 index 뷰를 연결합니다.
    path('<str:room_name>/', views.room, name='room'),
]