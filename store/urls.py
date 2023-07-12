from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.product_list, name='product_list'),
    path('products/<int:pk>/', views.product_detail, name='product_detail'),
    path('collections/', views.collection_list, name='collection-list'),
    path('collections/<int:pk>/', views.collection_detail,
         name='collection-detail'),

]
