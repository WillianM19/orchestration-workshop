from rest_framework import status
from rest_framework.response import Response
from .serializers import OrderSerializer
from rest_framework.views import APIView

class OrderCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = OrderSerializer(data=request.data)
        
        if serializer.is_valid():
            order = serializer.save()
            return Response({'order_id': order.id}, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)