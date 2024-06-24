from django.urls import path
from . import views

urlpatterns = [
    path('' , views.product_list , name='product_list') ,
    path('<int:pk>/' , views.product_detail , name='product_detail') ,
    path('create/' , views.product_create , name='product_create') ,
    # path('products/create/', views.product_create, name='product_create'),
    path('products/configure/<int:product_id>/' , views.configure_variants , name='configure_variants') ,
    path('shop-analysis/' , shop_analysis_view , name='shop_analysis') ,
    ]
