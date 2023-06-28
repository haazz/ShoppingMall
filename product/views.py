from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView
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

class ProductCreate(CreateView):
    model = Product
    fields = ['title', 'hook_text', 'content', 'head_image', 'category',]

"""
    def test_func(self):
        return self.request.user.is_superuser or self.request.user.is_staff
    def form_valid(self, form):
        current_user = self.request.user
        if current_user.is_authenticated and (current_user.is_staff or current_user.is_superuser):
            return super(ProductCreate, self).form_valid(form)
        else:
            return (redirect('/product/'))
"""

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
