from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    # url이 post를 포함해야 함 pk다음 오는 / 는 /가 한 번 더 와야 한다는 의미
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
