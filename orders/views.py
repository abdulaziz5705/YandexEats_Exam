from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from admin_app.permissions import IsCourier
from orders.models import OrderFromUser
from orders.serializers import OrderUserSerializer
from users.models import UserModel


class CourierToOrderView(APIView):

    permission_classes = [IsCourier]

    def patch(self, request, order_id):
        try:
            order = OrderFromUser.objects.get(id=order_id)
            courier = UserModel.objects.get(id=request.user.id, role='courier')
            if not courier:
                return Response(
                    {"error": "Only couriers can accept orders."},
                    status=status.HTTP_403_FORBIDDEN
                )

            if order.status == 'Pending' and order.courier is None:
                order.courier = courier
                order.status = 'Accepted by Courier'
            elif order.courier != courier:
                return Response(
                    {"error": "You are not assigned to this order."},
                    status=status.HTTP_403_FORBIDDEN
                )
            else:
                next_status = request.data.get('status')
                if next_status in dict(OrderFromUser.STATUS_CHOICES) and next_status != order.status:
                    order.status = next_status
                else:
                    return Response(
                        {"error": "Invalid or duplicate status update."},
                        status=status.HTTP_400_BAD_REQUEST
                    )

            order.save()
            return Response(OrderUserSerializer(order).data, status=status.HTTP_200_OK)
        except OrderFromUser.DoesNotExist:
            return Response({"error": "Order not found."}, status=status.HTTP_404_NOT_FOUND)





