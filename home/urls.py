from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static  
urlpatterns = [
    path('',views.home,name='home'),
    path('login/',views.login,name='login'),
    path('logout/', views.logout),
    path('signup/',views.signup,name='signup'),
    path('about/',views.about,name='about'),
    path('beauty/', views.beauty, name='beauty'),
    path('electronics/', views.electronics, name='electronics'),
    path('forms', views.forms, name='forms'),
    path('review', views.review,name='review'),
    path('recent-review/<int:num_posts>/', views.RecentReview, name='RecentReview'),
    path('review/<str:cat>/',views.custom_review),
        path('brand/create', views.BrandCreatePopup, name = "BrandCreatePopup"),
        path('city/create', views.CityCreatePopup, name = "CityCreatePopup"),
        path('product/create', views.ProductCreatePopup, name = "ProductCreatePopup"),
        path('place/create', views.PlaceCreatePopup, name = "PlaceCreatePopup"),
        path('places/', views.places,name='places'),
        path('getproducts/<str:brand>/',views.getproducts),
        path('getplaces/<str:city>/',views.getplaces),
]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
