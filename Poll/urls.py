from django.urls import path
from . import views

urlpatterns = [
    path('', views.WorkList.as_view(), name='work'),
    path('finish/', views.finish, name='finish')
]