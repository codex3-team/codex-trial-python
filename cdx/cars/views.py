from django.views.generic import View
from typing import Dict, Any

PAGINATION_NUM_ELEMENTS = 100


class CarView(View):
    def post(self, request, *args, **kwargs):
        return "HELLO"

    def get(self, request, *args, **kwargs):
        return "BYE!"