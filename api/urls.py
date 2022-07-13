from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name = 'api-overview'),
    path('task-list/', views.apitasklist, name = 'task-list' ),
    path('task-detail/<int:pk>/', views.apitaskdetail, name = 'task-detail' ),
    path('task-create/', views.apitaskcreate, name = 'task-create' ),
    path('task-update/<int:pk>/', views.apitaskupdate, name = 'task-update' ),
    path('task-delete/<int:pk>/', views.apitaskdelete, name = 'task-delete' ),
]