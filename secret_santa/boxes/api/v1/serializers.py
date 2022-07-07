from boxes.models import Boxes, GiftRequest, ReceiverSender
from rest_framework import serializers
from users.models import User


class BoxesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boxes
        fields = "__all__"


class GiftRequestSerializer(serializers.ModelSerializer):
    def to_representation(self, obj):
        ret = super().to_representation(obj)
        ret["user"] = UsersSerializer(obj.user).data
        ret["box"] = BoxesSerializer(obj.box).data
        return ret

    class Meta:
        model = GiftRequest
        fields = "__all__"


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "name"]

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
