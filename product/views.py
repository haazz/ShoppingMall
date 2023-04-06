from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Product, Category

class ProdcutDetail(DetailView):
    model = Product

class ProductList(ListView):
    model = Product
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(ProductList, self).get_context_data()
        context['categories'] = Category.objects.all()

        return context

def categories_page(request, slug):
    category = Category.objects.get(slug=slug)
    product_list = Product.objects.filter(category=category)
    context = {
        'category': category,
        'categories': Category.objects.all(),
        'category_product_count': Product.objects.filter(category=None).count(),
        'product_list': product_list,
    }
    return render(request, 'product/product_list.html', context)
