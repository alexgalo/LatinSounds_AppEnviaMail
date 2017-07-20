from django.shortcuts import render
from .forms import SendSong
from django.core.mail import EmailMultiAlternatives

# Create your views here.
def inicio(request):
    #definir situacion de envio
    info_enviado= False
    titulo= ""
    autor= ""
    letra= ""
    liga = ""
    if request.method == "POST":
        formulario = SendSong(request.POST)
        if formulario.is_valid():
            info_enviado = True
            titulo = formulario.cleaned_data['Titulo']
            autor = formulario.cleaned_data['Autor']
            letra = formulario.cleaned_data['Letra']
            liga = formulario.cleaned_data['Liga']

            #configuracion para enviar correo via gmail
            to_admin = 'tematico.2.1@gmail.com'
            html_content = " Mensaje de Usuario <br><br><br> *** Agrega esta cancion a Latin Sounds *** <br><br><br> <p>Cancion:%s</p> <p>Autor:%s</p> <p>Letra:</p>%s <p>URL imagen:%s</p><br>" %(titulo, autor, letra, liga)
            msg = EmailMultiAlternatives('Correo de contacto', html_content, 'from@server.com', [to_admin])
            msg.attach_alternative(html_content, 'text/html')
            msg.send()
    else:
        formulario = SendSong()

    form = SendSong(request.POST or None)
    context = {
        "form": form,
        "titulo": titulo,
        "autor": autor,
        "letra": letra,
        "liga": liga,
        "info_enviado": info_enviado
    }

    if form.is_valid():
        form_dicc= form.cleaned_data
        print form_dicc.get("titulo")


    return render(request, "inicio.html", context)
