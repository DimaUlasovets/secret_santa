import random
import uuid
from enum import Enum

from django.db import models

# Create your models here.


class StatusChoices(Enum):
    OPEN = "OPEN"
    MOVING = "MOVING"
    CLOSE = "CLOSE"

    @classmethod
    def choices(cls):
        return tuple((i.name.lower(), i.value) for i in cls)


class Users(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Boxes(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    name_box = models.CharField(max_length=100)
    create_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField(blank=True, null=True)
    status_box = models.CharField(max_length=10, choices=StatusChoices.choices(), default="open")

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
        if self.status_box == "moving":
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
        if self.status_box == "open" and len(self.users) > 2:
            self.status_box = "moving"
            self.move_bag()
            self.status_box = "close"
            self.save()


class GiftRequest(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    user = models.ForeignKey(Users, related_name="giftrequests", on_delete=models.CASCADE)
    description = models.TextField(null=True, blank=True)
    box = models.ForeignKey(Boxes, related_name="giftrequests", on_delete=models.CASCADE)


class ReceiverSender(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False, unique=True)
    sender = models.ForeignKey(Users, related_name="sender", on_delete=models.CASCADE)
    receiver = models.ForeignKey(Users, related_name="receiver", on_delete=models.CASCADE)
    box = models.ForeignKey(Boxes, on_delete=models.CASCADE)
