from django.urls import path

from orders import views
from orders.views import CourierToOrderView

urlpatterns = [
    path('<int:order_id>/courier/', views.CourierToOrderView.as_view(), name='assign-courier'),
]
