from rest_framework import serializers

from .models import Boxes, GiftRequest, ReceiverSender, Users


class BoxesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boxes
        fields = "__all__"


class GiftRequestSerializer(serializers.ModelSerializer):
    box = BoxesSerializer(many=False)

    class Meta:
        model = GiftRequest
        fields = "__all__"


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"

    def get_gifts(self, obj):
        gifts = obj.giftrequests.all()
        serializer = GiftRequestSerializer(gifts, many=True)
        return serializer.data


class ReceiverSenderSerializer(serializers.ModelSerializer):
    sender = UsersSerializer(many=False)
    receiver = UsersSerializer(many=False)
    box = BoxesSerializer(many=False)

    class Meta:
        model = ReceiverSender
        fields = "__all__"
