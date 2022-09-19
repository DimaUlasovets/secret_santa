from boxes import models, services, tasks
from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(pre_save, sender=models.Boxes)
def delete_receiver_sender_pairs(sender, instance=None, **kwargs):
    if instance.pk:
        receiver_sender_data = models.ReceiverSender.objects.filter(box=instance.pk)
        if instance.status_box == models.StatusChoices.OPEN and receiver_sender_data is not None:
            services.delete_receiver_sender_data(receiver_sender_data)
            tasks.message_change_pairs.delay(instance.pk)
