from django.urls import path
from .views import (CategoryListCreate, CategoryDetail, TypeListCreate, TypeDetail, ProductListCreate, ProductDetail, WireProductListCreate, WireProductDetail, CommentListCreate, CommentDetail, StockListCreate, StockDetail)

urlpatterns = [
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('types/', TypeListCreate.as_view(), name='type-list-create'),
    path('types/<int:pk>/', TypeDetail.as_view(), name='type-detail'),
    path('products/', ProductListCreate.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductDetail.as_view(), name='product-detail'),
    path('wireproducts/', WireProductListCreate.as_view(), name='wireproduct-list-create'),
    path('wireproducts/<int:pk>/', WireProductDetail.as_view(), name='wireproduct-detail'),
    path('comments/', CommentListCreate.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
    path('stocks/', StockListCreate.as_view(), name='stock-list-create'),
    path('stocks/<int:pk>/', StockDetail.as_view(), name='stock-detail'),
]
