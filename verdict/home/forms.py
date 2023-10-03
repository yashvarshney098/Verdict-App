from django import forms  
from .models import Electronic_Review,Place_Review ,Brand,Product,City, Place

class Electronic_ReviewForm(forms.ModelForm):  
    class Meta:  
        model = Electronic_Review
        fields = "__all__"
class Place_ReviewForm(forms.ModelForm):  
    class Meta:  
        model = Place_Review
        fields = "__all__"    
        exclude = ('category','date','product','brand','image')
class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'
class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
class CityForm(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'
class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = '__all__'