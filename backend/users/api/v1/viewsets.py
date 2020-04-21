from rest_framework import authentication
from users.models import HGgfh
from .serializers import HGgfhSerializer
from rest_framework import viewsets


class HGgfhViewSet(viewsets.ModelViewSet):
    serializer_class = HGgfhSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = HGgfh.objects.all()
