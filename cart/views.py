from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from product.models import Product


@login_required
def cart_detail(request):
    cart = request.session.get("cart", {})
    cart_items = []
    total = 0

    for product_id, item_data in cart.items():
        product = get_object_or_404(Product, id=product_id)
        quantity = item_data["quantity"]
        item_total = product.price * quantity
        cart_items.append(
            {
                "product": product,
                "quantity": quantity,
                "item_total": item_total,
                "quantity_plus": quantity + 1,
                "quantity_minus": quantity - 1,
            }
        )
        total += item_total

    return render(
        request,
        "cart/detail.html",
        {
            "cart_items": cart_items,
            "total": total,
        },
    )


@login_required
def cart_add(request, product_id):
    product = get_object_or_404(Product, id=product_id)

    if product.stock <= 0:
        messages.error(request, "Товара нет в наличии.")
        return redirect("product:product_detail", pk=product_id)

    cart = request.session.get("cart", {})
    current_qty = cart.get(str(product_id), {}).get("quantity", 0)

    if current_qty < product.stock:
        if str(product_id) in cart:
            cart[str(product_id)]["quantity"] += 1
        else:
            cart[str(product_id)] = {"quantity": 1}
        request.session["cart"] = cart
        request.session.modified = True
        messages.success(request, f"«{product.name}» добавлен в корзину!")
    else:
        messages.warning(
            request,
            f"Нельзя добавить больше {product.stock} шт. товара «{product.name}».",
        )

    return redirect("product:product_detail", pk=product_id)


@login_required
def cart_remove(request, product_id):
    cart = request.session.get("cart", {})
    cart.pop(str(product_id), None)
    request.session["cart"] = cart
    request.session.modified = True
    return redirect("cart:cart_detail")


@login_required
def cart_update(request, product_id):
    if request.method == "POST":
        try:
            quantity = int(request.POST.get("quantity", 1))
        except (TypeError, ValueError):
            quantity = 1

        if quantity < 1:
            quantity = 1

        product = get_object_or_404(Product, id=product_id)

        if quantity > product.stock:
            quantity = product.stock
            if quantity <= 0:
                return cart_remove(request, product_id)
            messages.warning(
                request,
                f"Нельзя добавить больше {product.stock} шт. товара «{product.name}».",
            )

        cart = request.session.get("cart", {})
        if str(product_id) in cart:
            cart[str(product_id)]["quantity"] = quantity
            request.session["cart"] = cart
            request.session.modified = True

    return redirect("cart:cart_detail")
