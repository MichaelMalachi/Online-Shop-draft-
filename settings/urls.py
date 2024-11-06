from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from product.views import (
    HomeView,
    CreateProduct,
    ProductListView,
    UserRegisterView,
    ProductUpdateView,
    ProductDeleteView,
    ProductDetailView,
    MyPageView,
    ProductViewSet,
)
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import obtain_auth_token

# Инициализируем роутер
router = routers.DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    # Ваши существующие маршруты
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

    # Маршруты для REST API
    path('api/', include(router.urls)),  # Let the router handle the API root
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]
