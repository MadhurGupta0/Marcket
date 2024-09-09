from django.shortcuts import render, get_object_or_404,redirect
from .models import CartItem
import home.models as mo
def add_to_cart(request, pk):
    product = get_object_or_404(mo.Item, pk=pk)
    user = request.user

    # Check if the product is already in the cart
    cart_item, created = CartItem.objects.get_or_create(user=user, item=product)
    cart_item.quantity += 1
    cart_item.save()
    return redirect('cart')
def cart(request):
    user = request.user
    cart_items = CartItem.objects.filter(user=user)
    total=0
    for i in cart_items:
        total+=i.item.price*i.quantity
    context = {
        'cart_items': cart_items,
        "total": total
    }
    return render(request, 'inbox.html', context)

def quantity_add(request,pk):
    item= get_object_or_404(mo.Item,pk=pk)
    cart_item = get_object_or_404(CartItem, item=item, user=request.user)

    if item.quantity-1>0:
      cart_item.quantity += 1
    cart_item.save()


    return redirect('cart')
def quantity_remove(request,pk):
    item= get_object_or_404(mo.Item,pk=pk)
    cart_item = get_object_or_404(CartItem, item=item, user=request.user)

    if cart_item.quantity-1>0:
      cart_item.quantity -= 1
      cart_item.save()
    else:
      cart_item.delete()
    return redirect('cart')