import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms


class Category(models.Model):
    category_title = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=False, default=timezone.now())
    

    @staticmethod
    def get_all_categories():
        return Category.objects.all()


    def __str__(self):
        return self.category_title




class Product(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    Created_at = models.DateTimeField(auto_now_add=False, default=timezone.now())
    price_1 = models.DecimalField(max_digits=10, decimal_places=2)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='static/shop/images')
    published = models.BooleanField(default=True)
    Featured = models.BooleanField(default=False)

    def __str__(self):
        return str(self.name) + ": Rs" + str(self.price)
        
    @staticmethod
    def get_products_by_id(ids):
        return Product.objects.filter(id__in =ids)

    @staticmethod
    def get_all_products():
        return Product.objects.all()

    @staticmethod
    def get_all_products_by_categoryid(category_id):
        if category_id:
            return Product.objects.filter(category = category_id)
        else:
            return Product.get_all_products();


class Contact(models.Model):
    contact_name = models.CharField(max_length=30)
    email = models.EmailField(max_length = 54)
    message = models.TextField(max_length=300)


    def __str__(self):
        return str(self.contact_name)

class UserCreateForm(UserCreationForm):
    email = forms.EmailField(required=True,label='Email',error_messages={'exists': 'This Already Exists'})

    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'confirm Password'

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError(self.fields['email'].error_message['exists'])
        return self.cleaned_data['email']



class Order(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    Addresss = models.TextField()
    Phone = models.IntegerField()
    Email = models.EmailField(max_length=100) 
    order_notes = models.TextField()
    amount = models.CharField(max_length=100)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username


class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    product = models.CharField(max_length=500)
    image = models.ImageField(upload_to='static/shop/img')
    quantity = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    

    def __str__(self):
        return self.order.user.username


