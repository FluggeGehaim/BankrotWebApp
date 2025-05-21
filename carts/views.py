from django.http import JsonResponse
from django.views import View

from carts.mixins import CartMixin
from goods.models import Lots
from .models import Cart


class CartAddView(CartMixin, View):
    def post(self, request):
        product_id = request.POST.get("product_id")
        lot = Lots.objects.get(id=product_id)

        cart = self.get_cart(request, lot=lot)

        if cart:
            cart.quantity += 1
            cart.save()
        else:
            Cart.objects.create(
                user=request.user if request.user.is_authenticated else None,
                session_key=(
                    request.session.session_key
                    if not request.user.is_authenticated
                    else None
                ),
                lot=lot,
                quantity=1,
            )

        response_data = {
            "message": "Товар добавлен в корзину",
            "cart_items_html": self.render_cart(request),
        }

        return JsonResponse(response_data)


class CartChangeView(CartMixin, View):
    def post(self, request):
        cart_id = request.POST.get("cart_id")
        cart = self.get_cart(request, cart_id=cart_id)
        cart.quantity = request.POST.get("quantity")
        cart.save()

        quantity = cart.quantity

        response_data = {
            "message": "Количество изменено",
            "cart_items_html": self.render_cart(request),
            "quantity": quantity,
        }

        return JsonResponse(response_data)


class CartRemoveView(CartMixin, View):
    def post(self, request):
        cart_id = request.POST.get("cart_id")
        cart = self.get_cart(request, cart_id=cart_id)
        quantity = cart.quantity
        cart.delete()

        response_data = {
            "message": "Товар удален",
            "quantity": quantity,
            "cart_items_html": self.render_cart(request),
        }

        return JsonResponse(response_data)
