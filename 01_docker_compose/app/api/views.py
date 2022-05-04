from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from api.pagination import CustomPagination  # isort:skip
from api.serializers import FilmworkSerializer  # isort:skip
from movies.models import Filmwork  # isort:skip


class FilmworkViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = FilmworkSerializer
    queryset = Filmwork.objects.all()
    permission_classes = [AllowAny]
    pagination_class = CustomPagination
