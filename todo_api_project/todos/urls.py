from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from .views import TodoViewSet, UserCreate

router = DefaultRouter()
router.register('todos', TodoViewSet, basename='todo')

urlpatterns = [
    path("user/new/", UserCreate.as_view(), name="user_create"),
    path('login/', views.obtain_auth_token, name='login'),
] + router.urls
