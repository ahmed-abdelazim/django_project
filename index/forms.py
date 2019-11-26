from django import forms
from .models import Cart

class Cart_Form(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(Cart_Form, self).__init__(*args, **kwargs)
        

    
    class Meta: # Hvilken model og felter vi ville have renderet på siden
        model = Cart
        fields = ['quantity']