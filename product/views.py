from django.db.models import Q
from django.views.generic import ListView, DetailView
from category.models import Category
from .models import Product


class ProductListView(ListView):
    model = Product
    template_name = "product/list.html"
    context_object_name = "products"
    paginate_by = 8

    def get_queryset(self):
        queryset = Product.objects.select_related("category").all()
        category_slug = self.kwargs.get("category_slug")
        query = self.request.GET.get("q", "").strip()

        if category_slug:
            queryset = queryset.filter(category__slug=category_slug)

        if query:
            queryset = queryset.filter(
                Q(name__icontains=query) | Q(description__icontains=query)
            )

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        context["selected_category"] = self.kwargs.get("category_slug")
        context["search_query"] = self.request.GET.get("q", "")
        return context


class ProductDetailView(DetailView):
    model = Product
    template_name = "product/detail.html"
    context_object_name = "product"
    pk_url_kwarg = "pk"
