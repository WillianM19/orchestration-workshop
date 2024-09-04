import requests
from rest_framework import views
from rest_framework.response import Response

class PurchaseProductView(views.APIView):

    def post(self, request, *args, **kwargs):
        product_id = request.data.get('product_id')
        quantity = request.data.get('quantity')

        try:
            response  = requests.get(f'http://localhost:8002/api/inventory/{product_id}')
            data = response.json()
            
            if data.get('stock', 0) < quantity:
                return Response({'error': f"Não há estoque suficiente para este pedido."}, status=400)
        
        except requests.RequestException:
            return Response({'error': 'Failed to create order'}, status=500)

        try:
            order_response = requests.post('http://localhost:8001/api/orders/', json={
                'product_id': product_id,
                'quantity': quantity
            })
            order_response.raise_for_status()

            if order_response.status_code != 200:
                return Response({'error': 'Failed to create order'}, status=400)

        except requests.RequestException:
            return Response({'error': 'Failed to create order'}, status=500)

        order_id = order_response.json().get('order_id')

        try:
            inventory_reserve_response = requests.post('http://localhost:8002/api/inventory/reserve/', json={
                'product_id': product_id,
                'quantity': quantity
            })
            inventory_reserve_response.raise_for_status()

            if inventory_reserve_response.status_code != 200:
                return Response({'error': 'Failed to reserve inventory'}, status=400)

        except requests.RequestException:
            return Response({'error': 'Failed to reserve inventory'}, status=500)

        try:
            response = requests.post(f'http://localhost:8003/api/payment/', json={
                'order_id': order_id,
                'value': data.get('product', 0)['price']
            })

            if response.status_code != 200:
                return Response({'error': 'Failed to reserve inventory'}, status=400)

        except requests.RequestException:
            return Response({'error': 'Failed to reserve inventory'}, status=500)

        return Response({'status': 'Pedido finalizado'})