from django.shortcuts import render
from .forms import ProductForm
from .models import Product, User
# Create your views here.

def index(request):
    context = {}
    return render(request, 'index.html', context=context)

def outofstock(request):
    current_user = User.objects.filter(username=request.user.username).all()
    if request.method == "POST":
        print("HELLOO")
        f = ProductForm( data=request.data,files=request.files)
        if f.is_valid():
            print("valid_form")
            f.save(commit=False)
            f.user_created = current_user
            f.save()
            return render(request, 'outofstock.html')


    query_set = Product.objects.filter(quantity=0, category__is_active=True).all()
    context = {'form' : ProductForm, 'products': query_set}
    return render(request, 'outofstock.html', context=context)
