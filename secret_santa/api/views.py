from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Boxes, GiftRequest, ReceiverSender, Users
from .serializers import (
    BoxesSerializer,
    GiftRequestSerializer,
    ReceiverSenderSerializer,
    UsersSerializer,
)


class RoutesList(APIView):
    """
    List all routes.
    """

    def get(self, request, format=None):
        routes = [
            {"GET": "/api/users"},
            {"GET": "/api/users/id"},
            {"GET": "/api/boxes"},
            {"GET": "/api/boxes/id"},
            {"GET": "/api/receiversender/id"},
            {"GET": "/api/receiversender"},
            {"GET": "/api/giftrequest/id"},
            {"GET": "/api/giftrequest"},
        ]
        return Response(routes)


class UsersList(APIView):
    """
    List all users.
    """

    def get(self, request, format=None):
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SingleUser(APIView):
    """
    Single user by id
    """

    def get_single_user(self, pk):
        return get_object_or_404(Users, pk=pk)

    def get(self, request, pk, format=None):
        user = self.get_single_user(pk)
        serializer = UsersSerializer(user, many=False)
        return Response(serializer.data)

    def patch(self, request, pk):
        user = self.get_single_user(pk)
        serializer = UsersSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        user = self.get_single_user(pk)
        serializer = UsersSerializer(user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_single_user(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BoxesList(APIView):
    """
    List all boxes.
    """

    def get(self, request, format=None):
        boxes = Boxes.objects.all()
        serializer = BoxesSerializer(boxes, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BoxesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SingleBox(APIView):
    """
    Single box by id
    """

    def get_single_box(self, pk):
        return get_object_or_404(Boxes, pk=pk)

    def get(self, request, pk, format=None):
        box = self.get_single_box(pk)
        serializer = BoxesSerializer(box, many=False)

        # group = get_object_or_404(Boxes, pk=pk)  # Test logic for close group and sort receiver/sender
        # group.close_group()  # Test logic for close group and sort receiver/sender

        return Response(serializer.data)

    def patch(self, request, pk):
        box = self.get_single_box(pk)
        serializer = BoxesSerializer(box, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        box = self.get_single_box(pk)
        serializer = BoxesSerializer(box, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        box = self.get_single_box(pk)
        box.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListReceiverSender(APIView):
    """
    List all Receiver/Sender
    """

    def get(self, request, format=None):
        receivers_senders = ReceiverSender.objects.all()
        serializer = ReceiverSenderSerializer(receivers_senders, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReceiverSender(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SingleReceiverSender(APIView):
    """
    Single receiver/sender by id
    """

    def get_single_receiver_sender(self, pk):
        return get_object_or_404(ReceiverSender, pk=pk)

    def get(self, request, pk, format=None):
        receiver_sender = self.get_single_receiver_sender(pk)
        serializer = ReceiverSenderSerializer(receiver_sender, many=False)
        return Response(serializer.data)

    def patch(self, request, pk):
        receiver_sender = self.get_single_receiver_sender(pk)
        serializer = ReceiverSenderSerializer(receiver_sender, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        receiver_sender = self.get_single_receiver_sender(pk)
        serializer = ReceiverSenderSerializer(receiver_sender, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        receiver_sender = self.get_single_receiver_sender(pk)
        receiver_sender.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListGiftRequest(APIView):
    """
    List all GiftRequest
    """

    def get(self, request, format=None):
        gift_request = GiftRequest.objects.select_related("box").all()
        serializer = GiftRequestSerializer(gift_request, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = GiftRequestSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SingleGiftRequest(APIView):
    """
    Single GiftRequest by id
    """

    def get_single_gift_request_sender(self, pk):
        return get_object_or_404(GiftRequest.objects.select_related("box"), pk=pk)

    def get(self, request, pk, format=None):
        gift_request = self.get_single_gift_request_sender(pk)
        serializer = GiftRequestSerializer(gift_request, many=False)
        return Response(serializer.data)

    def patch(self, request, pk):
        gift_request = self.get_single_gift_request_sender(pk)
        serializer = GiftRequestSerializer(gift_request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        gift_request = self.get_single_gift_request_sender(pk)
        serializer = GiftRequestSerializer(gift_request, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        gift_request = self.get_single_gift_request_sender(pk)
        gift_request.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
