from django import forms

class IndumentariaForm(forms.Form):
    nombre = forms.CharField(max_length= 80, required=True)
    marca = forms.CharField(max_length= 60, required=True)
    talle = forms.IntegerField(required=True)
    precio = forms.IntegerField(required=True)
    
class CalzadoForm(forms.Form):
    nombre = forms.CharField(max_length= 80, required=True)
    marca = forms.CharField(max_length= 60, required=True)
    talle = forms.IntegerField(required=True)
    precio = forms.IntegerField(required=True)
    
class AccesoriosForm(forms.Form):
    nombre = forms.CharField(max_length= 80, required=True)
    marca = forms.CharField(max_length= 60, required=True)
    descripcion = forms.CharField(max_length= 200,required=True)
    precio = forms.IntegerField(required=True)
    
class CochesForm(forms.Form):
    nombre = forms.CharField(max_length= 80, required=True)
    marca = forms.CharField(max_length= 60, required=True)
    descripcion = forms.CharField(max_length= 200,required=True)
    precio = forms.IntegerField(required=True)