
from django.urls import path
from .views import cart,add_to_cart,quantity_add,quantity_remove


urlpatterns = [
    path('cart/', cart,  name='cart'),
    path('<int:pk>/add_to_cart/',add_to_cart,name="add_to_cart"),
    path('<int:pk>/cart/add',quantity_add,name="quantity_add"),
    path('<int:pk>/cart/remove',quantity_remove,name="quantity_remove"),
]