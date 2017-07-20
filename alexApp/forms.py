from django import forms

class SendSong(forms.Form):
    Titulo= forms.CharField(max_length=150)
    Autor= forms.CharField(max_length=150)
    Letra= forms.CharField(widget=forms.Textarea)
    Liga= forms.URLField(label='URL de la imagen', required=False, initial='http://')
