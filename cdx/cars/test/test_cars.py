import pytest
from django.conf import settings
from rest_framework import status

from cdx.cars.models import Car


@pytest.fixture
def cars():
    for i in range(55):
        Car.objects.create(make='Pontiac' + str(i), model='GTO' + str(i), year=str(2021 - i))


@pytest.mark.django_db
def test_valid_post_send(client, cars):
    cars_count = Car.objects.count()
    page = (cars_count // settings.PAGINATION_NUM_COUNT) + 1
    remainder = cars_count % settings.PAGINATION_NUM_COUNT

    response = client.post('/cars', {'make': 'Test', 'model': 'Test', 'year': '1990'})
    assert response.status_code == 201
    response = client.get('/cars', {'page': page})
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == remainder + 1


@pytest.mark.django_db
def test_valid_get_send(client, cars):
    response = client.get('/cars/', {'page': '1'})
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 10

    response = client.get('/cars/', {})
    assert response.status_code == status.HTTP_200_OK
    assert len(response.data['results']) == 10


@pytest.mark.django_db
def test_invalid_get_send(client, cars):
    response = client.get('/cars/', {"page": "x"})
    assert response.status_code == status.HTTP_404_NOT_FOUND

    response = client.get('/cars/', {"page": "0"})
    assert response.status_code == status.HTTP_404_NOT_FOUND
