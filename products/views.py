from django.shortcuts import render, get_list_or_404, get_object_or_404,redirect
from django.http import JsonResponse
import json
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import *
from .forms import *

def Page_404(request, exception):
    
    return render(request, '404/404.html', {})

def handler500(request):
    return render(request, '404/500.html', status=500)

def index_view(request):
    categories = Category.objects.all()
    
    return render(request, 'products/index.html', {
        'categories':categories
        })

def category_view(request,category_slug):

    if request.user.is_authenticated:
        category =Category.objects.get(slug=category_slug)
        product = get_list_or_404(Products, category__id = category.id)
    else:
        return redirect('login_page')

    return render(request,'products/products.html',{
        'category' : category,
        'product' : product
    })

def addproduct_view(request):

    category =Category.objects.all()

    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            messages.success(request, "Profile save succesfully")

        else:
            messages.error(request, 'Incorrect information, please try again')
            return render (request, 'products/addproduct.html',{
                'form': form,
                'category' : category
            })
        
    form = AddProductForm()        
    return render (request, 'products/addproduct.html',{
        'form': form,
        'category' : category
    })

def delete_view(request, product_slug):
    product = get_object_or_404(Products,slug=product_slug)
    category =Category.objects.get(name = product.category)

    if request.method == 'POST':
        product.delete()
        messages.success(request, 'Product deleted')
        return redirect('index_page')

    return render (request, 'products/delete.html',{
        'product':product,
        'category':category

    })

def bag_view(request):
    bag = None
    bagitems = []

    if request.user.is_authenticated:
        bag, created = Bag.objects.get_or_create(user=request.user, completed=False)
        bagitems = bag.bagitems.all()
    return render(request, 'products/bag.html', {
        'bag':bag,
        'bagitems':bagitems
    })

def add_to_bag_view(request):
    data = json.loads(request.body.decode("utf-8"))
    prod_id = data["id"]
    product = Products.objects.get(id=prod_id)

    if request.user.is_authenticated:
        bag_view, created = Bag.objects.get_or_create(user=request.user, completed=False)
        bagItem, created = BagItem.objects.get_or_create(bag=bag_view, product=product)
        bagItem.quantity += 1
        bagItem.save()
        print(bagItem)

    return JsonResponse("working", safe=False)

def remove_from_bag_view(request, bag_item_id):
    if request.user.is_authenticated:
        bag_item = get_object_or_404(BagItem, id=bag_item_id, bag__user=request.user, bag__completed=False)
        bag_item.delete()
        messages.success(request, "The product has been deleted from the cart.")
        return redirect('bag_page')
    else:
        messages.error(request, 'Incorrect information, please try again')
        return redirect('bag_page')
