from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from rest_framework.response import Response
from app_cars.models import Car
from .serializers import CarSerializer
from rest_framework.permissions import AllowAny
from rest_framework.pagination import PageNumberPagination

import logging

logger = logging.getLogger('django')


@api_view(['GET', 'POST'])
@permission_classes([AllowAny])
def car_list(request):
    """
    List all cars or create a new entry.
    """
    if request.method == 'GET':
        paginator = PageNumberPagination()
        paginator.page_size = 10
        query_result = Car.objects.all()
        paginated_query_result = paginator.paginate_queryset(query_result, request)
        serializer = CarSerializer(paginated_query_result, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK )

    if request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)