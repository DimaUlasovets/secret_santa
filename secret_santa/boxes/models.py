import random
import uuid
from enum import Enum

from django.db import models
from users.models import User

# Create your models here.


class StatusChoices(str, Enum):
    OPEN = "open"
    MOVING = "moving"
    CLOSE = "close"

    @classmethod
    def choices(cls):
        return tuple((i.name.lower(), i.value) for i in cls)


class Boxes(models.Model):
    class Meta:
        verbose_name = "Box"
        verbose_name_plural = "Boxes"

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    name_box = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(blank=True, null=True)
    status_box = models.CharField(max_length=10, choices=StatusChoices.choices(), default=StatusChoices.OPEN)

    def __str__(self):
        return self.name_box

    @property
    def users(self):
        giftrequests = self.giftrequests.all()

        users = []
        for giftrequest in giftrequests:
            users.append(giftrequest.user)
        return users

    def move_bag(self):
        if self.status_box == StatusChoices.MOVING:
            giftrequests = self.giftrequests.all()
            users = self.users
            for giftrequest in giftrequests:
                secret_user = giftrequest.user
                while giftrequest.user == secret_user:
                    secret_user = random.choice(users)

                receiver_sender_data = ReceiverSender(
                    sender=giftrequest.user, receiver=secret_user, box=giftrequest.box
                )
                receiver_sender_data.save()

                users.remove(secret_user)

    def close_group(self):
        if self.status_box == StatusChoices.OPEN and len(self.users) > 2:
            self.status_box = StatusChoices.MOVING
            self.move_bag()
            self.status_box = StatusChoices.CLOSE
            self.save()


class GiftRequest(models.Model):
    class Meta:
        verbose_name = "Gift"
        verbose_name_plural = "Gifts"

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    user = models.ForeignKey(User, related_name="giftrequests", on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    box = models.ForeignKey(Boxes, related_name="giftrequests", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user} - {self.description}"


class ReceiverSender(models.Model):
    class Meta:
        verbose_name = "ReceiverSender"
        verbose_name_plural = "ReceiverSenders"

    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    sender = models.ForeignKey(User, related_name="sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name="receiver", on_delete=models.CASCADE)
    box = models.ForeignKey(Boxes, on_delete=models.CASCADE)
