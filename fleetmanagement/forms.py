from django import forms
from django.forms import TextInput, EmailInput,Select,DateField
from .models import Driver

class DriverForm(forms.ModelForm):

    class Meta:
        model=Driver
        fields = ['First_name', 'Last_name','Other_names','national_ID','address','Email','Phone_number','license_no','license_expiry_date','status']
        widgets = {
            'First_name': TextInput(attrs={
                'class': "form-control mb-5px",
                'placeholder': 'First Name'
                }),
            'Last_name': TextInput(attrs={
                'class': "form-control", 
                'placeholder': 'Last Name'
                }),
            'Other_names': TextInput(attrs={
                'class': "form-control", 
                'placeholder': 'Last Name'
                }),
            'national_ID': TextInput(attrs={
                'class': "form-control", 
                'placeholder': 'Last Name'
                }),
            'address': TextInput(attrs={
                'class': "form-control", 
                'placeholder': 'Last Name'
                }),
            'Email': EmailInput(attrs={
                'class': "form-control", 
                'placeholder': 'Last Name'
                }),
            'Phone_number': TextInput(attrs={
                'class': "form-control", 
                'placeholder': 'Last Name'
                }),
            'license_no': TextInput(attrs={
                'class': "form-control", 
                'placeholder': 'Last Name'
                }),
            'license_expiry_date': TextInput(attrs={
                'class':"form-control",
                'id':"datepicker-autoClose",
                'placeholder':"Select Date",
                'data-date-format':'yyyy-mm-dd' 
                
                }),
            'status': Select(attrs={
                'class': " selectpicker form-control", 
                'id':"ex-search"
                }),
        }
       
