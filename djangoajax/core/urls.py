from django.urls import path
from . import views

urlpatterns = [
        path('', views.home, name='home'),
        path('add', views.add_view, name='add'),
        #path('edit/<int:id>', views.edit_view, name='edit'),
        path('edit/update/<int:id>', views.update_student, name='update'),
        path('delete', views.delete_view, name='delete'),
        ]
