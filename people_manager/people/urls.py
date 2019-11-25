from rest_framework import routers
from .api import PeopleViewSet


# Use router to register relevant urls from ViewSet
router = routers.DefaultRouter()
router.register('api/people', PeopleViewSet, 'people')

# Defines patterns to be included from main urls.py
urlpatterns = router.urls
