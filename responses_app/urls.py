from django import views
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:id>', views.area, name='area'),
    path('new_place/<int:area_id>/', views.new_place, name='new_place'),
    path('delete/<int:pk>/', views.OrderDeleteView.as_view(), name='order_delete'),
    path('<int:pk>/comments', views.comments, name='comments'),    
    path('<int:place_id>/comment/update', views.comment_update, name='comment_update'),    
]