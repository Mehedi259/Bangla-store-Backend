from django.http import JsonResponse
from django.db.models import Sum, Count
from django.db.models.functions import TruncDate
from django.utils import timezone
from datetime import timedelta
from orders.models import Order
from products.models import Product


def dashboard_stats(request):
    now = timezone.now()
    this_month_start = now.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
    last_month_start = (this_month_start - timedelta(days=1)).replace(day=1)
    last_month_end = this_month_start

    this_orders = Order.objects.filter(created_at__gte=this_month_start)
    this_revenue = this_orders.aggregate(total=Sum('amount'))['total'] or 0
    this_order_count = this_orders.count()
    this_customers = this_orders.values('customer_name').distinct().count()

    last_orders = Order.objects.filter(created_at__gte=last_month_start, created_at__lt=last_month_end)
    last_revenue = last_orders.aggregate(total=Sum('amount'))['total'] or 0
    last_order_count = last_orders.count()
    last_customers = last_orders.values('customer_name').distinct().count()

    def trend(current, previous):
        if previous == 0:
            return "+100%" if current > 0 else "0%"
        pct = ((float(current) - float(previous)) / float(previous)) * 100
        sign = "+" if pct >= 0 else ""
        return f"{sign}{pct:.1f}%"

    total_products = Product.objects.count()
    all_revenue = Order.objects.aggregate(total=Sum('amount'))['total'] or 0
    all_orders = Order.objects.count()
    all_customers = Order.objects.values('customer_name').distinct().count()

    return JsonResponse({
        "totalRevenue": float(all_revenue),
        "totalOrders": all_orders,
        "totalCustomers": all_customers,
        "totalProducts": total_products,
        "trends": {
            "revenue": trend(this_revenue, last_revenue),
            "orders": trend(this_order_count, last_order_count),
            "customers": trend(this_customers, last_customers),
            "products": "+0%",
        }
    })


def sales_overview(request):
    now = timezone.now()
    start = now - timedelta(days=29)

    data = (
        Order.objects
        .filter(created_at__gte=start)
        .annotate(date=TruncDate('created_at'))
        .values('date')
        .annotate(revenue=Sum('amount'), orders=Count('id'))
        .order_by('date')
    )

    date_map = {}
    for item in data:
        label = item['date'].strftime('%d %b')
        date_map[label] = item

    result = []
    for i in range(30):
        day = (start + timedelta(days=i)).date()
        label = day.strftime('%d %b')
        entry = date_map.get(label)
        result.append({
            "name": label,
            "revenue": float(entry['revenue']) if entry else 0,
            "orders": entry['orders'] if entry else 0,
        })

    return JsonResponse(result, safe=False)


def order_status_stats(request):
    data = (
        Order.objects
        .values('status')
        .annotate(count=Count('id'))
        .order_by('-count')
    )
    return JsonResponse(list(data), safe=False)


def top_products(request):
    products = Product.objects.all()[:5]
    result = []
    for p in products:
        result.append({
            "id": p.id,
            "name": p.name,
            "price": float(p.price),
            "image": p.image,
            "category": p.category,
        })
    return JsonResponse(result, safe=False)


def recent_orders(request):
    orders = Order.objects.order_by('-created_at')[:5]
    result = []
    for o in orders:
        result.append({
            "id": o.id,
            "customer_name": o.customer_name,
            "customer_img": o.customer_img,
            "amount": float(o.amount),
            "payment_method": o.payment_method,
            "status": o.status,
            "created_at": o.created_at.isoformat(),
        })
    return JsonResponse(result, safe=False)
