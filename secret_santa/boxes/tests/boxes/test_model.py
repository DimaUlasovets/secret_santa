from boxes.models import Boxes, ReceiverSender


class TestGroup:
    def test_close_box(self, new_gift_request, new_users):
        """Close group"""
        box = Boxes.objects.get(name_box="Test_box_v2")
        box.close_group()

        receiver_senders = ReceiverSender.objects.filter(box=box)
        for receiver_sender in receiver_senders:
            assert receiver_sender.sender == receiver_sender.receiver
            assert box.status_box == "close"

    def test_move_bag_without_close_box(self, new_gift_request):
        """Move bag without close box"""
        box = Boxes.objects.get(name_box="Test_box_v2")
        box.move_bag()
        receiver_senders = ReceiverSender.objects.filter(box=box)
        for receiver_sender in receiver_senders:
            assert receiver_sender.receiver is None
            assert box.status_box == "open"
