from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from . import models
from .models import Brand, Product,Category,Place,City,Electronic_Review,Place_Review
from django.contrib.auth.models import User
from .forms import Electronic_ReviewForm, Place_ReviewForm,BrandForm,PlaceForm,ProductForm,CityForm
from django.views.decorators.csrf import csrf_exempt
import datetime
import json
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib import messages
from django.shortcuts import get_object_or_404

# Create your views here.
def login(req):
    if req.method=='GET':
        return render( req, 'home/login.html')
    # print('Login requested by user')
    email = req.POST['email']
    password = req.POST['password']
    # print('Logged in')
    if(User.objects.filter(username=email)):
        user = authenticate(username= email, password= password)
        if user is not None:
                req.session['message']  = email
                return redirect('/')
    messages.info(req,'Incorrect credentials')
    return render(req, 'home/login.html',{
        'logged' : 0
        })   
    
def signup(req):
    if req.method=='GET':
        return render( req, 'home/signup.html')
    # print('Login requested by user')
    email = req.POST['email']
    password = req.POST['password']
    if email=='' and password=='':
         return render( req, 'home/signup.html')
    try:
        email2 = User.objects.get(username=email)
    except :    
        email2 = None
    
    if email2 is not None:  
         return redirect('/login/')
    user = User.objects.create_user(username=email,password=password)
    user.save()
    # print('account created')
    return redirect('/login/')

def logout(request):
    del request.session['message']
    return redirect('/')   
    
def home(req):
    return render(req,'home/index.html')

def about(req):
    return render(req,'home/about.html' )

def electronics(request):
    return render(request, 'home/electronics.html' )

def beauty(request):
    return render(request, 'home/beauty.html' )

def places(req):
    return render(req,'home/restaurants.html')

def forms(request):
    brands = Brand.objects.all()
    product = Product.objects.all()
    category = Category.objects.all()
    return render(request,'home/forms.html',{
        'brand' : brands,
        'product' : product,
        'category' : category
    })

def review(request):  
    # review = ReviewForm()   
    brands = Brand.objects.all()
    product = Product.objects.all()
    category = Category.objects.all()
    return render(request,'home/review.html',{
        'brand' : brands,
        'product' : product,
        'category' : category,
        'form' : review
    })

def custom_review(req,cat):
    if req.method=='GET':
            if cat=='electronics' or cat=='beauty':
                flag = 0
            else:
                flag = 1
            brands = Brand.objects.filter( category__name__contains=cat)
            product = Product.objects.all()
            category = Category.objects.all()
            city = City.objects.all()
            place = Place.objects.all()
            email = ''
            if req.session.get('message', None):
                #  print('jjx')
                 email = req.session['message']
            return render(req,'home/custom_review.html',{
                'brand' : brands,
                'product' : product,
                'category' : category,
                'cat' :cat,
                'place' : place,
                'city':city,
                'email' : email,
                'flag' : flag
                })
    else:
        if cat=='electronics' or cat=='beauty':
            name= req.POST['name']
            email= req.POST['email']
            brand= Brand.objects.get(id=req.POST['brand'])
            product= Product.objects.get(id=req.POST.get("theInputGroup"))
            # print(req.POST.get("theInputGroup"))
            rating= req.POST['rating']
            review= req.POST['review']
            category = Category.objects.get(name=cat)
            # print(list(req.POST.items()))
            # print(list(req.FILES.items()))
            try: #if list(req.FILES.items()) == []: 
                image = req.FILES['image']
            except:
                image = ''  
            obj = Electronic_Review(name=name, mail = email,category = category,brand=brand,product=product,rating=rating,review=review,image=image)
            obj.save()
        else:
                name= req.POST['name']
                email= req.POST['email']
                city= City.objects.get(id=req.POST['city'])
                place= Place.objects.get(id=req.POST.get("theInputGroup")) 
                rating= req.POST['rating']
                review= req.POST['review']
                category = Category.objects.get(name=cat)
                try: #if list(req.FILES.items()) == []: 
                    image = req.FILES['image']
                except:
                    image = ''  
                obj = Place_Review(name=name, mail = email,category = category,city=city,place=place,rating=rating,review=review,image=image)
                obj.save()
        return redirect('/review',{
            'create' : 'success'
        })
def BrandCreatePopup(request):
	form = BrandForm(request.POST or None)
	if form.is_valid():
		instance = form.save()
		## Change the value of the "#id_brand". This is the element id in the form
		return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_brand");</script>' % (instance.pk, instance))
	return render(request, "home/popup_form.html", {"form" : form})

def ProductCreatePopup(request):
	form = ProductForm(request.POST or None)
	if form.is_valid():
		instance = form.save()
		## Change the value of the "#id_brand". This is the element id in the form
		return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_brand");</script>' % (instance.pk, instance))
	return render(request, "home/popup_form.html", {"form" : form})

def CityCreatePopup(request):
	form = CityForm(request.POST or None)
	if form.is_valid():
		instance = form.save()
		## Change the value of the "#id_brand". This is the element id in the form
		return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_brand");</script>' % (instance.pk, instance))
	return render(request, "home/popup_form.html", {"form" : form})

def PlaceCreatePopup(request):
	form = PlaceForm(request.POST or None)
	if form.is_valid():
		instance = form.save()
		## Change the value of the "#id_brand". This is the element id in the form
		return HttpResponse('<script>opener.closePopup(window, "%s", "%s", "#id_brand");</script>' % (instance.pk, instance))
	return render(request, "home/popup_form.html", {"form" : form})


def RecentReview(req,num_posts):
        upper = num_posts
        # print(num_posts)
        lower = upper - 3
        elec = list(Electronic_Review.objects.all().order_by('-id').values()[lower:upper])
        print(elec)
        place= list(Place_Review.objects.all().order_by('-id').values()[lower:upper])
        brands = list(Brand.objects.all())
        products = list(Product.objects.all())
        # print(elec)
        # print(brands,products)
        for i in elec:
            i['brand_id'] = Brand.objects.get(id = i['brand_id']).name
            i['product_id'] = Product.objects.get(id = i['product_id']).name
            i['date'] = str(i['date'])[:11]
            if i['image']=='':
                i['image'] = 'reviews/default.png'
        for i in place:
            i['city_id'] = City.objects.get(id = i['city_id']).name
            i['place_id'] = Place.objects.get(id = i['place_id']).name
            i['date'] = str(i['date'])[:11]
            if i['image']=='':
                i['image'] = 'reviews/default.png'
            # i['product_id'] = brands[i['product_id']]
        # print(elec)
        # print(place)
        posts_size = len(Electronic_Review.objects.all()) + len(Place_Review.objects.all())
        max_size = True if upper >= posts_size else False
        return JsonResponse({'elec': elec,'place' : place, 'max': max_size}, safe=False)


@csrf_exempt
def get_author_id(request):
	if request.is_ajax():
		brand_name = request.GET['brand_name']
		brand_id = Brand.objects.get(name = brand_name).id
		data = {'brand_id':brand_id,}
		return HttpResponse(json.dumps(data), content_type='application/json')
	return HttpResponse("/")

def getproducts(req, brand):
    # print(brand)
    brands = Brand.objects.get_or_create(name=brand)
    # print(brands)
    products = Product.objects.filter(brand = brands[0].id)
    product_ids = [ i.id for i in products]
    # print(product_ids)
    
    reviews = []
    prod_avg_rating = {}
    for i in product_ids:
        item = Electronic_Review.objects.filter(product = int(i))
        if item:
            s = 0
            count = 0
            name=''
            for j in item:
                name = j.product
                if j.image=='':
                    j.image = 'reviews/default.png'
                j.image  = 'images/'+str(j.image) 
                s += j.rating
                count+=1
            prod_avg_rating[name]  = round(s/count,1)
            print(prod_avg_rating)
            for k in item:
                reviews.append(k)
    # print(list(reviews))
    
    return render(req,'home/getproducts.html',{
        'reviews' : reviews,
        'Brand' : brand,
        'prod_avg_rating' : prod_avg_rating
    })
    
def getplaces(req, city):
    # print(city)
    cities = City.objects.get_or_create(name=city)
    places = Place.objects.filter(city = cities[0].id)
    places_ids = [ i.id for i in places]
    reviews = []
    place_avg_rating = {}
    for i in places_ids:
        item = Place_Review.objects.filter(place = int(i))
        if item:
            s = 0
            count = 0
            name=''
            for j in item:
                if j.image=='':
                    name = j.place
                    j.image = 'reviews/default.png'
                j.image  = 'images/'+str(j.image) 
                s += j.rating
                count+=1
            print(item)
            place_avg_rating[name]  = round(s/count,1)
            for k in item:
                reviews.append(k)
    # print(list(reviews))
    return render(req,'home/getplaces.html',{
        'reviews' : reviews,
        'City' : city,
        'place_avg_rating' : place_avg_rating
    })