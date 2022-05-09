from django.shortcuts import render
from django.shortcuts import redirect
from requests import request
from .models import  Product
from .models import Category
from .models import Contact
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
from .models import UserCreateForm
from .models import Order
from .models import OrderItem
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def home(request):
    product = Product.objects.filter(Featured=True)
    product2 = Product.objects.all().order_by('-Created_at')
    categories = Category.get_all_categories()
    params={
            'product': product,
            'categories': categories,
            'product2': product2,           
}
    return render(request, 'index.html', params)



def about(request):
    categories = Category.get_all_categories()
    params={
            'categories': categories,
}
    return render(request,"about.html", params)


def contact(request):
    if request.method=="POST":
        contact_name=request.POST['contact_name']
        email=request.POST['email']
        message =request.POST['message']
        contact=Contact(contact_name=contact_name, email=email, message=message)
        contact.save()
    categories = Category.get_all_categories()
    return render(request,"contact.html", {'categories': categories})


def store(request):
    product = Product.objects.filter(published=True)
    categories = Category.get_all_categories()
    paginator = Paginator(product, 22) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params={
            'product': page_obj,
            'page_obj':page_obj,
            'categories': categories,
}
    return render(request,"store.html", params)


def recent(request):
    product = Product.objects.filter(published=True).order_by('-Created_at')
    categories = Category.get_all_categories()
    paginator = Paginator(product, 22) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params={
            'product': page_obj,
            'page_obj':page_obj,
            'categories': categories,
}
    return render(request,"store.html", params)


def category(request):
    categories = Category.get_all_categories()
    categoryID = request.GET.get('category')
    if categoryID:
        Products = Product.get_all_products_by_categoryid(categoryID)
    else:
        Products = None
    params={
            'categories': categories,
             'product':Products ,
}
    return render(request,"category.html", params)



def view(request, id):
    product = Product.objects.filter(id=id)
    categories = Category.get_all_categories()
    params={ 
            'product':product,
            'categories': categories,
}
    return render(request,"view.html", params)



@login_required(login_url="/accounts/login")
def cart_add(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def item_clear(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.remove(product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def item_increment(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.add(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def item_decrement(request, id):
    cart = Cart(request)
    product = Product.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("cart_detail")


@login_required(login_url="/accounts/login")
def cart_detail(request):
    categories = Category.get_all_categories()
    params={ 
            
            'categories': categories,
    }
    return render(request, 'cart/cart_detail.html', params)



def signup(request):
    categories = Category.get_all_categories()
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            new_user = authenticate(
                username = form.cleaned_data['username'],
                password = form.cleaned_data['password1'],
            )
            login(request,new_user)
            return redirect('/')
    else:
        form = UserCreateForm()

    context = {
        'form':form,
        'categories': categories,
    }
    return render(request,'registration/signup.html',context)

def check(request):
    categories = Category.get_all_categories()
    context = {
        'categories': categories,
    }
    return render(request,'checkout.html', context)

def checkout(request):
    categories = Category.get_all_categories()
    if request.method=="POST":
        uid = request.session.get('_auth_user_id', '')
        user = User.objects.get(id = uid)
        cart = request.session.get('cart', '')
        f_name = request.POST.get('f_name', '')
        l_name = request.POST.get('l_name', '')
        Addresss = request.POST.get('Addresss', '')
        Email = request.POST.get('Email', '')
        order_notes = request.POST.get('order_notes', '')
        amount= request.POST.get('amount', '')
        Phone= request.POST.get('Phone', '')
        order = Order( f_name=f_name, l_name=l_name, Addresss=Addresss, Email=Email,
                      amount=amount, order_notes=order_notes, Phone=Phone, user=user)
        order.save()
        for i in cart:
            item = OrderItem(
                order = order,
                product = cart[i]['name'],
                image = cart[i]['image'],
                quantity = cart[i]['quantity'],
                price = cart[i]['price'],  
            )
            item.save()
    context = {
        'categories': categories,
    }
    return render(request, 'thankyou.html', context)
    


def search(request):
    querry = request.GET.get('querry')
    product = Product.objects.filter(published=True ,name__icontains = querry)
    categories = Category.get_all_categories()
    paginator = Paginator(product, 22) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    params={
            'product': page_obj,
            'page_obj':page_obj,
            'categories': categories,
}
    return render(request,"store.html", params)
