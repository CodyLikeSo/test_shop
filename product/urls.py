# product/urls.py
from django.urls import path
from . import views
from product.views import ProductListView, ProductDetailView

app_name = "product"

urlpatterns = [
    path("", views.ProductListView.as_view(), name="product_list"),
    path(
        "category/<slug:category_slug>/",
        views.ProductListView.as_view(),
        name="product_list_by_category",
    ),
    path("<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
]
