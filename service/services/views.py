from django.db.models import Prefetch
from rest_framework.viewsets import ReadOnlyModelViewSet

from clients.models import Client
from services.models import Subscriptions
from services.serializers import SubscriptionSerializer


class SubscriptionView(ReadOnlyModelViewSet):
    # Предотвращение дублирования запросов в БД - prefetch_related.
    # Выбираем какие данные доставать.
    queryset = Subscriptions.objects.all().prefetch_related(
        Prefetch(
            'client',
            queryset=Client.objects.all().select_related('user').only('company_name', 'user__email')
        )
    )
    serializer_class = SubscriptionSerializer
