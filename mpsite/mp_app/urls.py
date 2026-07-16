from rest_framework import routers
from django.urls import path, include
from .views import LogoutView,  RegisterView,CustomLoginView,UserProfileViewSet


router = routers.SimpleRouter()
router.register('user', UserProfileViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register_list'),
    path('login/', CustomLoginView.as_view(), name='login_list'),
    path('logout/', LogoutView.as_view(), name='logout_list')
]