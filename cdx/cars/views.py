from django.http import JsonResponse
from django.views.generic import View
from rest_framework import status

from cdx.cars.models import Car
from cdx.cars.utils import CarSerializer

PAGINATION_NUM_ELEMENTS = 10


class CarView(View):
    def post(self, request):
        serializer = CarSerializer(data=request.POST)
        if serializer.is_valid():
            kwargs = serializer.data
            Car.objects.create(**kwargs)
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return JsonResponse("This request must contain make<str>, model<str>, year<int>",
                                status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        page = request.GET.get("page")
        if page:
            try:
                page = int(page)
            except (TypeError, ValueError):
                return JsonResponse("Page argument is not a valid digit value", status=400, safe=False)
        else:
            return JsonResponse("Page argument for GET request is missed", status=400, safe=False)

        if not page:
            return JsonResponse("Page argument for GET equals to 0", status=400, safe=False)

        lbound = PAGINATION_NUM_ELEMENTS * (page - 1) + 1
        ubound = PAGINATION_NUM_ELEMENTS * page
        qs = Car.objects.filter(idx_id__gte=lbound, idx_id__lte=ubound)
        json = CarSerializer(qs, many=True).data
        return JsonResponse(json, status=200, safe=False)
