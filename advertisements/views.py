from rest_framework.permissions import IsAuthenticated
from rest_framework.viewsets import ModelViewSet

from advertisements.filters import AdvertisementFilter
from advertisements.permissions import IsAdminOrReadOnly
from advertisements.serializers import AdvertisementSerializer
from advertisements.models import Advertisement


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    # TODO: настройте ViewSet, укажите атрибуты для кверисета,
    queryset = Advertisement.objects.all()

    # TODO: сериализаторов и фильтров

    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter
    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create", "update", "partial_update", "destroy"]:
            return [IsAuthenticated(), IsAdminOrReadOnly(), ]
        return []
