from django.views.generic import TemplateView
from product.models import Products
from django.views.generic import ListView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.urls import reverse_lazy
from django.views.generic import CreateView
from product.models import CustomUser123
from .forms import UserRegisterForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView

class MyPageView(LoginRequiredMixin, TemplateView):
    template_name = 'my_page.html'


class UserRegisterView(SuccessMessageMixin, CreateView):
    model = CustomUser123
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')
    success_message = "Аккаунт успешно создан!"






class HomeView(TemplateView):
    template_name = 'home.html'



class CreateProduct(CreateView):
    model = Products
    fields = ['name', 'description', 'price']
    success_url = reverse_lazy('product-link')
    template_name = 'create.html'

class ProductListView(ListView):
    model = Products
    template_name = 'product.html'  # Шаблон для отображения списка продуктов
    context_object_name = 'products'

class ProductUpdateView(UpdateView):
    model = Products
    fields = ['name', 'description', 'price']
    template_name = 'update_product.html'
    success_url = reverse_lazy('product-link')

class ProductDeleteView(DeleteView):
    model = Products
    template_name = 'delete_product.html'
    success_url = reverse_lazy('product-link')

class ProductDetailView(DetailView):
    model = Products
    template_name = 'product_detail.html'
    context_object_name = 'product'

