# cms_app/urls.py
# cms_app/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, ContentItemViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'content-items', ContentItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api/content-items/create/', ContentItemViewSet.as_view({'post': 'create'}), name='contentitem-create'),
]
