from django.views.generic.list import ListView

from .filters import TruckFilter
from .models import Truck


class TrucksView(ListView):
    template_name = "trucks/main.html"
    model = Truck

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["filter"] = TruckFilter(self.request.GET, self.get_queryset())
        return context
