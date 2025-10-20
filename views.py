from django.http import JsonResponse
from django.shortcuts import render



# Create your views here.
products=[
    {'id':1,'name':'product1','cost':230},
    {'id':2,'name':'product2','cost':240},
    {'id':3,'name':'product3','cost':250},
    {'id':4,'name':'product4','cost':260},
    {'id':5,'name':'product5','cost':270},
]

# To add new data
def products_view(req):
    print("Hi")
    if req.method =='POST':
        p_name=req.POST.get('product_name')
        p_cost=req.POST.get('cost')
        id=len(products) + 1
        new_prod = {
            'id':id,
            'name':p_name,
            'cost':p_cost
        }
        products.append(new_prod)
            
    return render(req,'home.html',{'products':products})