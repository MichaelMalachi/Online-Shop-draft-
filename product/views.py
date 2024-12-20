from django.views.generic import TemplateView
from product.models import Products
from django.views.generic import ListView, UpdateView, DeleteView, DetailView, CreateView
from django.urls import reverse_lazy
from product.models import CustomUser123
from .forms import UserRegisterForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework import viewsets
from .serializers import ProductSerializer
from .tasks import send_welcome_email

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Products.objects.all()
    serializer_class = ProductSerializer



class MyPageView(LoginRequiredMixin, TemplateView):
    template_name = 'my_page.html'

# views.py
from django.core.mail import send_mail

class UserRegisterView(SuccessMessageMixin, CreateView):
    model = CustomUser123
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')
    success_message = "Аккаунт успешно создан!"

    def form_valid(self, form):
        response = super().form_valid(form)
        # Отправка приветственного письма
        send_mail(
            'Добро пожаловать на наш сайт!',
            'Спасибо за регистрацию.',
            'no-reply@mysite.com',
            [self.object.email],
            fail_silently=False,
        )
        return response


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

class UserRegisterView(SuccessMessageMixin, CreateView):
    model = CustomUser123
    form_class = UserRegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('home')
    success_message = "Аккаунт успешно создан!"

    def form_valid(self, form):
        response = super().form_valid(form)
        # Отправка приветственного письма через Celery
        send_welcome_email.delay(self.object.email)
        return response
