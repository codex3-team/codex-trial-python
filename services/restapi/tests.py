import os
import tempfile

import pytest
from pydantic import ValidationError

from cars.serializers import CarSerializer

def test_successfull_validation():
        CarSerializer(**{
                    "make": "Test",
                    "model": "Rich3",
                    "year": "2021"
                })


def test_negative_not_enough_fields():
    with pytest.raises(ValidationError):
        CarSerializer(**{
                    "make": "Test",
                    "year": "2021"
                })


def test_negative_long_year():
    with pytest.raises(ValidationError):
        CarSerializer(**{
                    "make": "Test",
                    "model": "Rich3",
                    "year": "20212"
                })

        