from rest_framework import serializers

from services.models import Subscriptions, Plan


class PlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plan
        fields = '__all__'


class SubscriptionSerializer(serializers.ModelSerializer):
    # Вложенный сериализатор.
    plan = PlanSerializer()
    client_name = serializers.CharField(source='client.company_name')
    email = serializers.CharField(source='client.user.email')
    # Ищет функцию get_price.
    price = serializers.SerializerMethodField()

    def get_price(self, instance):
        # Формула вычисления процента.
        return instance.service.full_price - instance.service.full_price * (instance.plan.discount_percent / 100)

    class Meta:
        model = Subscriptions
        fields = ('id', 'plan_id', 'client_name', 'email', 'plan')











