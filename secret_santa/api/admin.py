from django.contrib import admin

from .models import Boxes, GiftRequest, ReceiverSender, Users

# Register your models here.


admin.site.register(Users)
admin.site.register(Boxes)
admin.site.register(GiftRequest)
admin.site.register(ReceiverSender)
