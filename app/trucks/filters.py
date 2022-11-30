import django_filters

from .models import Truck, TruckType


class TruckFilter(django_filters.FilterSet):

    vehicle_type = django_filters.ModelChoiceFilter(
        queryset=TruckType.objects.all(),
    )

    class Meta:
        model = Truck
        fields = [
            "vehicle_type",
        ]
