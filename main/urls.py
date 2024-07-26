from django.urls import path
from .views import *

urlpatterns = [
    path('', TaskList.as_view(), name='task-list'),
    path('<int:pk>/', TaskDetail.as_view(), name='task-detail')
]
