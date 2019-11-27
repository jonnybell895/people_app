from rest_framework import permissions, viewsets, mixins
from .serializers import PeopleSerializer
from people.models import People


class PeopleViewSet(viewsets.ModelViewSet, mixins.ListModelMixin):
    """
    People ViewSet

    Implements basic Get, Post, Delete, Patch API for People model
    """
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = PeopleSerializer

    def get_queryset(self):
        return People.objects.all().order_by(self.request.GET.get('order_by', 'name'))
