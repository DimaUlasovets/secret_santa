from boxes import models
from celery import shared_task

from .celery.inform_using_mail import send_mail_to


@shared_task
def message_to_receiver_sender(pk):
    box = models.Boxes.objects.get(id=pk)
    receiver_sender = models.ReceiverSender.objects.filter(box=pk)
    for el in receiver_sender:
        description = models.GiftRequest.objects.filter(user=el.receiver, box=pk).first().description
        mail_subject = "Secret santa email"
        mail_message = f"You pair in {box.name_box} are: {el.receiver} and he/she wants {description}"
        to_email = el.sender
        send_mail_to(mail_subject, mail_message, to_email)
    return "Mail pairs sended"


@shared_task
def message_change_pairs(pk):
    receiver_sender = models.ReceiverSender.objects.filter(box=pk)
    for el in receiver_sender:
        mail_subject = "Secret santa email"
        mail_message = "Sorry, box status changed and we will give you a new pair"
        to_email = el.sender
        send_mail_to(mail_subject, mail_message, to_email)
    return "Mail cahnge pairs sended"
