from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from store import views
from django .views.static import serve

urlpatterns = [
    path("", views.store, name='store'),
    
    path("recent/", views.recent, name='recents'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("category/", views.category, name='category'),
    path("productview/<int:id>", views.view, name='view'),
    path("home/", views.home, name='home'),
    path("checkout/", views.checkout, name='checkout'),
    path("check/", views.check, name='check'),
    path("search/", views.search, name='search'),
    
     path('signup',views.signup,name='signup'),
    path('accounts/',include('django.contrib.auth.urls')),
    

    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),
    
    
    
    
]