import pytest
from pytest_factoryboy import register

from .factories import BoxesFactory, GiftRequestFactory, UsersFactory

register(BoxesFactory)
register(UsersFactory)
register(GiftRequestFactory)


@pytest.fixture
def new_users(db, users_factory):
    users = users_factory.create_batch(5)
    return users


@pytest.fixture
def new_box(db, boxes_factory):
    box = boxes_factory.create()
    return box


@pytest.fixture
def new_gift_request(db, gift_request_factory):
    gift_request = gift_request_factory.create()
    return gift_request
