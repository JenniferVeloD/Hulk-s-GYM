from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.urls import reverse

def login_view(request):
    """
    View para que un usuario pueda iniciar sesión
    """
    if request.method == 'POST':
        """
        Si la solicitud es POST, significa que el usuario ha enviado el formulario de inicio de sesión
        """
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():
            """
            Si el formulario es válido (las credenciales son correctas)
            """
            user = form.get_user()
            """
            Obtiene el objeto de usuario autenticado
            """
            login(request, user)
            """
            Inicia la sesión del usuario
            """
            return redirect(reverse('admin:index'))
            """
            Redirige al admin de Django
            """
    else:
        """
        Si la solicitud no es POST
        """
        form = AuthenticationForm()
        """
        Crea una instancia vacía del formulario de autenticación
        """

    return render(request, 'login.html', {'form': form})
    """
    Renderiza la plantilla 'login.html', pasándole el formulario al contexto
    """
