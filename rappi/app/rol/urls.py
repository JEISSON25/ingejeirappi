from django.urls import path

from . import views

urlpatterns = [
    path('api/rol', views.RolView.as_view(),
         name='Rollist'),
    path('api/rol/create/', views.CreateRolView.as_view(),
         name='CreateRollist')
]