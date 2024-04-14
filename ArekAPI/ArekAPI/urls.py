from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from UserValidation.views import UserProfileViewSet

router = routers.DefaultRouter()
router.register('user', UserProfileViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
]
