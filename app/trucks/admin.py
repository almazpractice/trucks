from django.contrib import admin


from .models import Truck, TruckType


@admin.register(TruckType)
class TruckTypeAdmin(admin.ModelAdmin):
    list_display = ("pk", "name", "load_capacity")
    list_display_links = ("pk", "name")
    list_editable = ("load_capacity",)
    search_fields = ("name",)
    empty_value_display = "-пусто-"


@admin.register(Truck)
class TruckAdmin(admin.ModelAdmin):
    list_display = ("pk", "board_number", "vehicle_type", "cur_load")
    list_display_links = ("pk", "board_number")
    list_editable = ("cur_load", "vehicle_type")
    search_fields = ("board_number",)
    empty_value_display = "-пусто-"
