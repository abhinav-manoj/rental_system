from django import forms
from .models import HomeDetails

class HomeForm(forms.ModelForm):
    class Meta:
        model = HomeDetails
        fields = '__all__'
        widgets = {
            "owner":forms.Select(attrs={'class': 'form-control', 'id': 'property_type_dropdown' ,'style':'width:400px;'}),
            "property_type": forms.Textarea(attrs={"cols":30,"rows":3,'class':'form-control','style':'width:400px;'}),
            "location": forms.Textarea(attrs={"cols": 30, "rows": 3,'class':'form-control','style':'width:400px;'}),
            "description": forms.Textarea(attrs={"cols":30,"rows":3,'class':'form-control','style':'width:400px;'}),
            "price_per_month": forms.TextInput(attrs={'class':'form-control','style':'width:400px;'}),
            "number_of_bedrooms": forms.TextInput(attrs={'class':'form-control','style':'width:400px;'}),
            "number_of_bathrooms": forms.TextInput(attrs={'class':'form-control','style':'width:400px;'}),
            "square_footage": forms.TextInput(attrs={'class':'form-control','style':'width:400px;'}),
            "available_from": forms.DateInput(attrs={'type': 'date' ,'class':'form-control','style':'width:400px;'}),
            "contact_number": forms.NumberInput(attrs={'class':'form-control','style':'width:400px;'}),
            
            'image': forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'image/*','style':'width:400px;'}),
            'email_id':forms.TextInput(attrs={'placeholder': 'Enter your email',
            'class': 'email-input form-control',
            'style':'width:400px;'})
            
        }
      
