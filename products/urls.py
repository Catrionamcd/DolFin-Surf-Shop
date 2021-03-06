"""
    Urls for products app
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_products, name='products'),
    path('update_session/', views.update_session, name='update_session'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_product, name='add_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),  # noqa
    path('add_product_comment/<int:product_id>/', views.add_product_comment, name='add_product_comment'),  # noqa
    path('edit_product_comment/<int:product_id>/', views.edit_product_comment, name='edit_product_comment'),  # noqa
    path('delete_product_comment/<int:product_id>/', views.delete_product_comment, name='delete_product_comment'),  # noqa
]
