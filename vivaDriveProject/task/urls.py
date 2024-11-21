from django.urls import path

from . import views
from .views import IndexView

app_name = 'task'
urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/delete/', views.delete, name='delete'),
]