from django.shortcuts import render
from django.views import View
#from django.http import HttpResponse
from base.products import products


# Create your views here.

class Home(View):
    def get(self,request):
        return render(request, 'hello.html',{})
        #return HttpResponse("<h1>Ce site represente un catalloque de produit</h1>")

class ProductList(View):
    def get(self,request):
        return render(request, 'ListProducts.html',{'produits':products})