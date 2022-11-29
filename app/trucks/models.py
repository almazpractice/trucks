from django.db import models


class TruckType(models.Model):
    name = models.CharField(max_length=50, db_index=True)
    load_capacity = models.PositiveIntegerField()

    class Meta:
        verbose_name = "Тип самосвала"
        verbose_name_plural = "Типы самосвала"

    def __str__(self) -> str:
        return self.name


class Truck(models.Model):
    board_number = models.CharField(max_length=20, db_index=True)
    vehicle_type = models.ForeignKey(
        TruckType,
        on_delete=models.CASCADE,
        related_name="truck",
    )
    cur_capacity = models.PositiveIntegerField()

    def get_overload(self):
        load_capacity = self.vehicle_type.load_capacity
        overload = (self.cur_capacity - load_capacity) * 100 / load_capacity
        return f"{overload:.1f}%" if overload > 0 else "-"

    class Meta:
        verbose_name = "Самосвал"
        verbose_name_plural = "Самосвалы"

    def __str__(self) -> str:
        return self.board_number
