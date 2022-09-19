from boxes import tasks
from boxes.api.v1.serializers import (
    BoxCommentsSerializer,
    BoxesSerializer,
    GiftRequestSerializer,
    ReceiverSenderSerializer,
    UsersSerializer,
)
from boxes.models import BoxComments, Boxes, GiftRequest, ReceiverSender
from boxes.paginations import PaginationHandlerMixin
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.exceptions import ValidationError
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from users.models import User


class BasicPagination(PageNumberPagination):
    page_size_query_param = "limit"


class RoutesList(APIView):
    """
    List all routes.
    """

    def get(self, request, format=None):
        routes = [
            {"GET": "/v1/boxes/users"},
            {"GET": "/v1/boxes/users/id"},
            {"GET": "/v1/boxes/boxes"},
            {"GET": "/v1/boxes/boxes/id"},
            {"GET": "/v1/boxes/receiversenders/id"},
            {"GET": "/v1/boxes/receiversenders"},
            {"GET": "/v1/boxes/giftrequests/id"},
            {"GET": "/v1/boxes/giftrequests"},
        ]
        return Response(routes)


class UsersList(APIView, PaginationHandlerMixin):
    """
    List all users.
    """

    permission_classes = [AllowAny]
    pagination_class = BasicPagination

    def get(self, request, format=None):
        users = User.objects.all()
        page = self.paginate_queryset(users)

        if page is not None:
            serializer = self.get_paginated_response(UsersSerializer(page, many=True).data)
        else:
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
        return get_object_or_404(User, pk=pk)

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


class BoxesList(APIView, PaginationHandlerMixin):
    """
    List all boxes.
    """

    permission_classes = [AllowAny]
    pagination_class = BasicPagination

    def get(self, request, format=None):
        status_box = self.request.query_params.get("status_box", None)
        boxes = Boxes.objects.all()

        if status_box:
            boxes = boxes.filter(status_box=status_box)

        page = self.paginate_queryset(boxes)

        if page is not None:
            serializer = self.get_paginated_response(BoxesSerializer(page, many=True).data)
        else:
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


class CloseBox(APIView):
    """
    Close box, change status box to close
    """

    def get(self, request, pk, format=None):
        box = get_object_or_404(Boxes, pk=pk)
        box.close_group()
        tasks.message_to_receiver_sender.delay(pk)
        return Response(status.HTTP_200_OK)


class ListReceiverSender(APIView, PaginationHandlerMixin):
    """
    List all Receiver/Sender
    """

    permission_classes = [AllowAny]
    pagination_class = BasicPagination

    def get(self, request, format=None):

        sender = self.request.query_params.get("sender", None)
        receiver = self.request.query_params.get("receiver", None)
        box = self.request.query_params.get("box", None)

        receivers_senders = ReceiverSender.objects.all()

        if sender:
            receivers_senders = receivers_senders.filter(sender__email__contains=sender)
        if receiver:
            receivers_senders = receivers_senders.filter(receiver__email__contains=receiver)
        if box:
            receivers_senders = receivers_senders.filter(box__name_box__contains=box)

        page = self.paginate_queryset(receivers_senders)

        if page is not None:
            serializer = self.get_paginated_response(ReceiverSenderSerializer(page, many=True).data)
        else:
            serializer = ReceiverSenderSerializer(receivers_senders, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ReceiverSenderSerializer(data=request.data)
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


class ListGiftRequest(APIView, PaginationHandlerMixin):
    """
    List all GiftRequest
    """

    permission_classes = [AllowAny]
    pagination_class = BasicPagination

    def get(self, request, format=None):

        box = self.request.query_params.get("box", None)
        user = self.request.query_params.get("user", None)

        gift_request = GiftRequest.objects.select_related("box").all()

        if box:
            gift_request = gift_request.filter(box__name_box__contains=box)
        if user:
            gift_request = gift_request.filter(user__email__contains=user)

        page = self.paginate_queryset(gift_request)

        if page is not None:
            serializer = self.get_paginated_response(GiftRequestSerializer(page, many=True).data)
        else:
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


class BoxesComments(APIView, PaginationHandlerMixin):
    """
    List all comments.
    """

    permission_classes = [AllowAny]
    pagination_class = BasicPagination

    def get(self, request, format=None):
        box = self.request.query_params.get("box", None)
        box_comments = BoxComments.objects.filter(user=self.request.user)

        if box:
            box_comments = box_comments.filter(box=box)

        page = self.paginate_queryset(box_comments)

        if page is not None:
            serializer = self.get_paginated_response(BoxCommentsSerializer(page, many=True).data)
        else:
            serializer = BoxCommentsSerializer(box_comments, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = BoxCommentsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SingleCommentBox(APIView):
    """
    Single box by id
    """

    def get_single_comment(self, pk):
        return get_object_or_404(BoxComments, pk=pk)

    def get(self, request, pk, format=None):
        comment = self.get_single_comment(pk)
        serializer = BoxCommentsSerializer(comment, many=False)
        return Response(serializer.data)

    def patch(self, request, pk):
        comment = self.get_single_comment(pk)
        serializer = BoxCommentsSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk, format=None):
        comment = self.get_single_comment(pk)
        serializer = BoxCommentsSerializer(comment, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        comment = self.get_single_comment(pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
