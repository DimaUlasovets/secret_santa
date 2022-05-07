from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("", views.RoutesList.as_view()),
    path("users/", views.UsersList.as_view()),
    path("users/<uuid:pk>", views.SingleUser.as_view()),
    path("boxes/", views.BoxesList.as_view()),
    path("boxes/<uuid:pk>", views.SingleBox.as_view()),
    path("receiversender/", views.ListReceiverSender.as_view()),
    path("receiversender/<uuid:pk>", views.SingleReceiverSender.as_view()),
]
urlpatterns = format_suffix_patterns(urlpatterns)
