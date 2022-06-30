from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("", views.RoutesList.as_view()),
    path("users/", views.UsersList.as_view(), name="users_list_api"),
    path("users/<uuid:pk>", views.SingleUser.as_view(), name="users_detail_api"),
    path("boxes/", views.BoxesList.as_view(), name="boxes_list_api"),
    path("boxes/<uuid:pk>", views.SingleBox.as_view(), name="boxes_detail_api"),
    path("receiversender/", views.ListReceiverSender.as_view(), name="receiversender_list_api"),
    path("receiversender/<uuid:pk>", views.SingleReceiverSender.as_view(), name="receiversender_detail_api"),
    path("giftrequest/", views.ListGiftRequest.as_view(), name="giftrequest_list_api"),
    path("giftrequest/<uuid:pk>", views.SingleGiftRequest.as_view(), name="giftrequest_detail_api"),
]
urlpatterns = format_suffix_patterns(urlpatterns)
