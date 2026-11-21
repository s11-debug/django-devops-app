from django.http import HttpResponse

def list_products(request):
    # BUG: missing import for Product model, will crash at runtime
    products = Product.objects.all()
    html = "<ul>"
    for product in products:
        html += f"<li>{product.name} - ${product.price}</li>"
    html += "</ul>"
    return HttpResponse(html)

