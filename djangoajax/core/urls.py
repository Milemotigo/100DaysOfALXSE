from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('add', views.add_view, name='add'),
        path('update', views.update_view, name='update'),
        path('delete', views.delete_view, name='delete'),
        ]
