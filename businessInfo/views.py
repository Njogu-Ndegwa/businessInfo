from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import BusinessInfo
from .serializers import BusinessInfoSerializer


@api_view(['GET', 'POST'])
def business_list(request):
    """
    List all business, or create a new business.
    """

    if request.method == 'GET':
        business = BusinessInfo.objects.all()
        serializer = BusinessInfoSerializer(business, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = BusinessInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)