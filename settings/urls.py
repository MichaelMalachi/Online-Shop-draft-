
from django.contrib import admin
from django.urls import path
from product.views import HomeView
from django.contrib.auth import views as auth_views
from product.views import CreateProduct
from product.views import ProductListView
from product.views import UserRegisterView
from product.views import ProductUpdateView, ProductDeleteView, ProductDetailView
from product.views import MyPageView


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', CreateProduct.as_view(), name='create-link'),
    path('register/', UserRegisterView.as_view(), name='register'),
    path('products/', ProductListView.as_view(), name='product-link'),
    path('products/update/<int:pk>/', ProductUpdateView.as_view(), name='product-update'),
    path('products/delete/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('my-page/', MyPageView.as_view(), name='my_page'),
    path('admin/', admin.site.urls),
]
