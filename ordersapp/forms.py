from .models import Orders,Payment,Pets,OrderPet
from django import forms


class OrderForm(forms.ModelForm):
    states = [
        ('AP','Andhra Pradesh'),
        ('AR','Arunachal Pradesh'),
        ('MH','Maharashtra'),
        ('RJ','Rajasthan'),
        ('UP','Uttar Pradesh'),
        ('GJ','Gujrat'),
        ('AS','Assam'),
        ('BR','Bihar')
    ]
    
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    phone = forms.CharField(max_length=10,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    email = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    address = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    state = forms.CharField(widget=forms.Select(choices=states,attrs={'class' : 'form-control'}))
    city = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    country = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class' : 'form-control'}))
    class Meta:
        model = Orders
        fields = ['first_name','last_name','phone','email','address','city','state','country']