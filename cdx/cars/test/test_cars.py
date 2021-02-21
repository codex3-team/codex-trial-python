from cdx.cars.models import Car
from rest_framework import status
import pytest
from cdx.cars.views import PAGINATION_NUM_ELEMENTS
from django.db import connection


@pytest.fixture
def cars():
    for i in range(55):
        Car.objects.create(make='Pontiac' + str(i), model='GTO' + str(i), year=str(2021 - i))


@pytest.fixture
def reset_sequences():
    with connection.cursor() as cursor:
        cursor.execute("ALTER SEQUENCE idx_id_seq RESTART WITH 1;")


@pytest.mark.django_db
def test_valid_post_send(client, cars):
    cars_count = Car.objects.count()
    page = (cars_count // PAGINATION_NUM_ELEMENTS) + 1
    remainder = cars_count % PAGINATION_NUM_ELEMENTS

    response = client.post('/cars/', {'make': 'Test', 'model': 'Test', 'year': '1990'})
    assert response.status_code == 201
    response = client.get('/cars/', {'page': page})
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == remainder + 1


@pytest.mark.django_db
def test_valid_get_send(client, reset_sequences, cars):
    response = client.get('/cars/', {'page': '1'})
    assert response.status_code == status.HTTP_200_OK
    assert len(response.json()) == 10


@pytest.mark.django_db
@pytest.mark.parametrize(
    'data',
    (
            ({}),
            ({"page": 0}),
            ({"page": "x"}),
    )
)
def test_invalid_get_send(data, client, reset_sequences, cars):
    response = client.get('/cars/', data)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
