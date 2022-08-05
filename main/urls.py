from django.urls import path, include
from .  import views
urlpatterns = [
    path('',views.index),
    path('ad',views.numver),
    path('adi',views.ad)
]