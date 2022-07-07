from boxes.models import Boxes, GiftRequest, ReceiverSender
from django.contrib import admin

# Register your models here.


@admin.register(Boxes)
class BoxesAdmin(admin.ModelAdmin):
    pass


@admin.register(GiftRequest)
class GiftRequestAdmin(admin.ModelAdmin):
    pass


@admin.register(ReceiverSender)
class ReceiverSenderAdmin(admin.ModelAdmin):
    pass
