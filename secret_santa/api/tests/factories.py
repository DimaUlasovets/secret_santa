import factory
from faker import Faker

from ..models import Boxes, GiftRequest, Users

fake = Faker()


class BoxesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Boxes

    name_box = "Test_box_v2"


class UsersFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Users

    first_name = factory.LazyAttribute(lambda _: fake.first_name())
    last_name = factory.LazyAttribute(lambda _: fake.last_name())
    email = factory.LazyAttribute(lambda _: fake.email())


class GiftRequestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GiftRequest

    user = factory.SubFactory(UsersFactory)
    description = fake.word()
    box = factory.SubFactory(BoxesFactory)
