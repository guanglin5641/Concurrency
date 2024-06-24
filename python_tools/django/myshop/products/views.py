from django.shortcuts import render , get_object_or_404 , redirect
from .models import Product
from .forms import ProductForm , VariantTypeForm , VariantForm


def product_list(request) :
    products = Product.objects.all()
    return render(request , 'products/product_list.html' , { 'products' : products })


def product_detail(request , pk) :
    product = get_object_or_404(Product , pk=pk)
    variants = product.variants.all()
    return render(request , 'products/product_detail.html' , { 'product' : product , 'variants' : variants })


def product_create(request) :
    if request.method == 'POST' :
        form = ProductForm(request.POST)
        if form.is_valid() :
            product = form.save()
            return redirect('configure_variants' , product_id=product.id)
    else :
        form = ProductForm()
    return render(request , 'products/product_form.html' , { 'form' : form })


def configure_variants(request , product_id) :
    product = Product.objects.get(id=product_id)
    if request.method == 'POST' :
        type_form = VariantTypeForm(request.POST)
        variant_form = VariantForm(request.POST)
        if type_form.is_valid() and variant_form.is_valid() :
            variant_type = type_form.save()
            variant = variant_form.save(commit=False)
            variant.product = product
            variant.type = variant_type
            variant.save()
    else :
        type_form = VariantTypeForm()
        variant_form = VariantForm()
    return render(request , 'products/configure_variants.html' ,
                  { 'product' : product , 'type_form' : type_form , 'variant_form' : variant_form })
