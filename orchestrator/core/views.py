import requests
from rest_framework import views
from rest_framework.response import Response

class PurchaseProductView(views.APIView):

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')

        try:
            inventory_check_response = requests.get(f'http://localhost:8002/api/inventory/{product_id}/')
            inventory_check_response.raise_for_status()

            inventory_data = inventory_check_response.json()
            if inventory_data['quantity'] < quantity:
                return Response({'error': 'Product not available in inventory'}, status=400)
        except requests.RequestException:
            return Response({'error': 'Failed to check inventory'}, status=500)

        try:
            order_response = requests.post('http://localhost:8001/api/orders/', json={
                'product_id': product_id,
                'quantity': quantity
            })
            order_response.raise_for_status()

            if order_response.status_code != 201:
                return Response({'error': 'Failed to create order'}, status=400)

            order_id = order_response.json().get('order_id')
        except requests.RequestException:
            return Response({'error': 'Failed to create order'}, status=500)

        try:
            inventory_reserve_response = requests.post('http://localhost:8002/api/inventory/', json={
                'product_id': product_id,
                'quantity': quantity
            })
            inventory_reserve_response.raise_for_status()

            if inventory_reserve_response.status_code != 201:
                return Response({'error': 'Failed to reserve inventory'}, status=400)
        except requests.RequestException:
            return Response({'error': 'Failed to reserve inventory'}, status=500)

        try:
            payment_response = requests.post('http://localhost:8003/api/payments/', json={
                'order_id': order_id,
                'value': quantity * 10
            })
            payment_response.raise_for_status()

            if payment_response.status_code != 200:
                requests.put(f'http://localhost:8002/api/inventory/{product_id}/', json={
                    'quantity': quantity
                })
                return Response({'error': 'Failed to process payment'}, status=400)
        except requests.RequestException:
            requests.put(f'http://localhost:8002/api/inventory/{product_id}/', json={
                'quantity': quantity
            })
            return Response({'error': 'Failed to process payment'}, status=500)

        return Response({'status': 'Purchase Completed'})
