from boxes.api.v1 import endpoints
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path("", endpoints.RoutesList.as_view()),
    path("users/", endpoints.UsersList.as_view(), name="users_list_api"),
    path("users/<str:pk>", endpoints.SingleUser.as_view(), name="users_detail_api"),
    path("boxes/", endpoints.BoxesList.as_view(), name="boxes_list_api"),
    path("boxes/<uuid:pk>", endpoints.SingleBox.as_view(), name="boxes_detail_api"),
    path("receiversenders/", endpoints.ListReceiverSender.as_view(), name="receiversender_list_api"),
    path("receiversenders/<uuid:pk>", endpoints.SingleReceiverSender.as_view(), name="receiversender_detail_api"),
    path("giftrequests/", endpoints.ListGiftRequest.as_view(), name="giftrequest_list_api"),
    path("giftrequests/<uuid:pk>", endpoints.SingleGiftRequest.as_view(), name="giftrequest_detail_api"),
]
urlpatterns = format_suffix_patterns(urlpatterns)
