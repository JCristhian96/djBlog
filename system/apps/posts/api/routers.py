from rest_framework.routers import DefaultRouter
# ViewSets
from . import viewsets

router = DefaultRouter()

router.register('posts', viewsets.PostViewSet, basename="posts")

urlpatterns = router.urls