from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('add-product/', views.AddProductView.as_view(), name='add-product'),
    path('product-list/', views.ProductListView.as_view(), name='product-list'),
    path('edit-product/<int:pk>/', views.EditProductView.as_view(), name='edit-product')
]