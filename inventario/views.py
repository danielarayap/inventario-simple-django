from django.shortcuts import render
from .models import Product


def index(request):
	latest_products = Product.objects.order_by('-pub_date')[:12]

	context = {
		'latest_products': latest_products,
	}

	if request.POST.get("add", False):
		product = request.POST["product"]
		instance = Product()
		instance.producto = product
		instance.amount = 5
		instance.save()

	if request.POST.get("remove", False):
		instance = Product.objects.get(id=request.POST["remove"])
		instance.delete()

	if request.POST.get("plus", False):
		instance = Product.objects.get(id=request.POST["plus"])
		instance.amount +=1
		instance.save()

	if request.POST.get("minus", False):
		instance = Product.objects.get(id=request.POST["minus"])
		instance.amount -=1
		instance.save()

	return render(request, 'inventario/index.html', context)




