from django.db.models import F
from django.shortcuts import render

from .forms import TruckForm
from .models import Truck


def get_overload(obj):
    load_capacity = obj.vehicle_type.load_capacity
    overload = (obj.cur_capacity - load_capacity) * 100 / load_capacity
    return f"{overload:.1f}%" if overload > 0 else "-"


def main(request):
    form = TruckForm(request.POST or None)
    trucks = Truck.objects.all().annotate(
        overload=(F("cur_capacity") - F("vehicle_type__load_capacity"))
        * 100
        / F("vehicle_type__load_capacity")
    )
    if form.is_valid():
        trucks = Truck.objects.filter(
            vehicle_type=form.data.get("vehicle_type"),
        ).annotate(
            overload=(F("cur_capacity") - F("vehicle_type__load_capacity"))
            * 100
            / F("vehicle_type__load_capacity")
        )
        context = {"form": form, "trucks": trucks}
        return render(request, "trucks/main.html", context)
    context = {"form": form, "trucks": trucks}
    return render(request, "trucks/main.html", context)
