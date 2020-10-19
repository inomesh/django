from django.http  import HttpResponse, JsonResponse, Http404
from django.http import request
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from .forms import ProductForm
from .models import Products

# Create your views here.

# def bad_view(request, *args, **kwargs):

#     #{'view_product': ['True'], 'title': ["Don't"], 'content': ['This is not great']}
#     my_request_data = dict(request.GET)
#     new_product     = my_request_data.get("view_product")
#     print(my_request_data, new_product)
#     if new_product[0].lower() == 'true':

#         Products.objects.create(title=my_request_data.get("title")[0],
#         content=my_request_data.get("content")[0])
#     return HttpResponse("Don't do this")


def home_view(request, *args, **kwargs):    # "/"
    return render(request, "homepage.html")




def search_view(request, *args, **kwargs):    #/search/
    # return  HttpResponse("<h1>hello world</h1>")

    try:
        query = request.GET.get("q") #q
        qs    = Products.objects.filter(title__icontains=query[0])

        print(query, qs)
        context = {"name": "Lucifer", "query":query}
    except:
        context = {"name": "Lucifer"}

    return render(request, "home.html", context)


# def product_create_view(request, *args, **kwargs):
#     # print("POST --> ",request.POST)
#     # print("GET  --> ",request.GET)

#     if request.method == "POST":
#         post_data = request.POST or None
#         if post_data != None:
#             my_form = ProductForm(request.POST)
#             if my_form.is_valid():
#                 title_from_input = my_form.cleaned_data.get("title")
#                 Products.objects.create(title=title_from_input)
#     return render(request, "forms.html")

@staff_member_required
def product_create_view(request, *args, **kwargs):
    
    form = ProductForm(request.POST or None)
   
    if form.is_valid():
        
        obj = form.save(commit=False)
        # do some stuff here
        obj.user = request.user

        obj.save()
        # print(form.cleaned_data)
        # data = form.cleaned_data
        # Products.objects.create(**data) #**data means keyword arguments.
        form = ProductForm()    #re-initializing the form   
       
    return render(request, "forms.html",{"form":form})









# def Product_detail_view(request, *args, **kwargs):
def Product_detail_view(request, pk):
    try:
        obj = Products.objects.get(pk=pk)    
    except:
        raise Http404
    # return HttpResponse(f'Object ID is {obj.id}')
    return render(request, "products/detail.html", {"object":obj})

# def Product_api_detail_view(request, *args, **kwargs):
def Product_api_detail_view(request,pk,*args, **kwargs):
    # obj = Products.objects.get(id=1)    
    try:
        obj = Products.objects.get(pk=pk)    
    except:
        return JsonResponse({"message": "Not Found"}) 
    return JsonResponse({
        "id": obj.id
    })



def Product_list_view(request, *args, **kwargs):
    qs = Products.objects.all()
    context = {"object_list":qs}
    return render(request,"Products/list.html", context)