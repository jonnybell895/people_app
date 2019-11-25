from rest_framework import permissions, viewsets
from .serializers import PeopleSerializer
from people.models import People


class PeopleViewSet(viewsets.ModelViewSet):
    """
    People ViewSet

    Implements basic Get, Post, Delete, Patch API for People model
    """
    permission_classes = [
        permissions.AllowAny
    ]
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
