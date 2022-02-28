from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from userapp.views import UserCreateList, UserGDU
from feed.views import MediaCreate, MediaDelete, PostViewSet, LikeDelete, LikeCreateList

r = DefaultRouter()
r.register("post", PostViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/<int:pk>/', UserGDU.as_view()),
    path('like/<int:pk>/', LikeDelete.as_view()),
    path('media/<int:pk>/', MediaDelete.as_view()),
    path('media/', MediaCreate.as_view()),
    path('like/', LikeCreateList.as_view()),
    path('user/', UserCreateList.as_view()),
    path('', include(r.urls)),
]



