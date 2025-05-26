from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('watchitems/', views.watchitem_index, name='watchitem_index'),
    path('watchitems/<int:pk>/', views.watchitem_detail, name='watchitem_detail'),
    path('watchitems/create/', views.WatchItemCreate.as_view(), name='watchitem_create'),
    path('watchitems/<int:pk>/update/', views.WatchItemUpdate.as_view(), name='watchitem_update'),
    path('watchitems/<int:pk>/delete/', views.WatchItemDelete.as_view(), name='watchitem_delete'),
]

