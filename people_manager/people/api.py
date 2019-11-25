from rest_framework import permissions, viewsets
from .serializers import PeopleSerializer
from people.models import People


class PeopleViewSet(viewsets.ModelViewSet):
    permission_classes = [
        permissions.AllowAny
    ]
    queryset = People.objects.all()
    serializer_class = PeopleSerializer
