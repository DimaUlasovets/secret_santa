from boxes.api.v1.serializers import BoxesSerializer, GiftRequestSerializer
from boxes.models import Boxes, GiftRequest
from django.urls import reverse
from faker import Faker
from rest_framework import status
from rest_framework.test import APITestCase
from users.models import User


class SecretSantaTestCase(APITestCase):
    def setUp(self):
        fake = Faker()

        for i in range(3):
            user = User.objects.create(name=fake.name(), email=fake.email())
            user.save()

        self.user = user
        self.box = Boxes.objects.create(name_box="Test_box")

        for user in User.objects.all():
            description = fake.word()
            self.giftrequest = GiftRequest.objects.create(user=user, box=self.box, description=description)


class BoxesAPITests(SecretSantaTestCase):
    def test_list_boxes_check_page(self):
        """
        List boxes
        """
        url = "/api/v1/boxes/"

        with self.assertNumQueries(1):
            response = self.client.get(url)

        boxes = Boxes.objects.all()
        serializer = BoxesSerializer(boxes, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response.data, serializer.data)

    def test_new_box_check_page(self):
        """
        New box
        """
        url = reverse("boxes_list_api")
        data = {"name_box": "Test"}
        with self.assertNumQueries(1):
            response = self.client.post(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_new_group_send_status(self):
        """
        New boz, return status box
        """
        url = reverse("boxes_list_api")
        data = {"name_box": "Test", "status": "close"}
        with self.assertNumQueries(1):
            response = self.client.post(url, data, format="json")

        box = response.json()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(box["status_box"], "open")


class BoxesDetailAPITests(SecretSantaTestCase):
    def test_detail_boxes_check_page(self):
        """
        Detail box by id
        """
        url = f"/api/v1/boxes/{self.box.id}"

        with self.assertNumQueries(1):
            response = self.client.get(url)

        box = Boxes.objects.get(pk=self.box.id)
        serializer = BoxesSerializer(box)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response.data, serializer.data)

    def test_change_box_name(self):
        """
        Change box name
        """
        data = {"name_box": "Test_box_v2"}
        box = Boxes.objects.get(name_box="Test_box")
        url = reverse("boxes_detail_api", args=(box.id,))
        with self.assertNumQueries(2):
            response = self.client.put(url, data, format="json")

        box = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(box["name_box"], "Test_box_v2")

    def test_change_status_box(self):
        """
        Change box status
        """
        data = {"name_box": "Test_box", "status_box": "close"}
        box = Boxes.objects.get(name_box="Test_box")
        url = reverse("boxes_detail_api", args=(box.id,))
        with self.assertNumQueries(2):
            response = self.client.patch(url, data, format="json")

        box = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(box["status_box"], "close")


class GiftRequestAPITests(SecretSantaTestCase):
    def test_list_giftrequest_check_page(self):
        """
        List GiftRequest
        """
        url = "/api/v1/giftrequests/"

        with self.assertNumQueries(1):
            response = self.client.get(url)

        gift_requests = GiftRequest.objects.select_related("box").all()
        serializer = GiftRequestSerializer(gift_requests, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response.data, serializer.data)


class GiftRequestDetailAPITests(SecretSantaTestCase):
    def test_detail_giftrequest_check_page(self):
        """
        Detail GiftRequest by id
        """
        url = f"/api/v1/giftrequests/{self.giftrequest.id}"

        with self.assertNumQueries(1):
            response = self.client.get(url)

        gift_requests = GiftRequest.objects.select_related("box").get(pk=self.giftrequest.id)
        serializer = GiftRequestSerializer(gift_requests)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.headers["Content-Type"], "application/json")
        self.assertEqual(response.data, serializer.data)
