from django.urls import path
from . import views

urlpatterns = [
    path('stats/', views.dashboard_stats),
    path('sales-overview/', views.sales_overview),
    path('order-status/', views.order_status_stats),
    path('top-products/', views.top_products),
    path('recent-orders/', views.recent_orders),
]
