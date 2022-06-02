from django import forms


class form_Usuario(forms.Form):
      nombre = forms.CharField(max_length=40)
      email = forms.EmailField()
      contraseña = forms.CharField(max_length=20)
      
      
class form_inicio(forms.Form):
      
      email = forms.EmailField()
      contraseña = forms.CharField(max_length=20)
      
      

class form_texto(forms.Form):
      nombre = forms.CharField(max_length=40)
      texto = forms.CharField(widget=forms.Textarea)
      

class form_personas(forms.Form):
    nombre = forms.CharField(max_length=40)
    apellido = forms.CharField(max_length=40)
    nacionalidad = forms.CharField(max_length=20)
    edad = forms.IntegerField()