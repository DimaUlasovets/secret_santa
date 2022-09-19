import factory
from boxes.models import Boxes, GiftRequest
from faker import Faker
from users.models import User

fake = Faker()


class BoxesFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Boxes

    name_box = "Test_box_v2"


class UsersFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    name = factory.LazyAttribute(lambda _: fake.name())
    # last_name = factory.LazyAttribute(lambda _: fake.last_name())
    email = factory.LazyAttribute(lambda _: fake.email())


class GiftRequestFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = GiftRequest

    user = factory.SubFactory(UsersFactory)
    description = fake.word()
    box = factory.SubFactory(BoxesFactory)
