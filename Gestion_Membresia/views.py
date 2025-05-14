from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages 


# Create your views here.

def agregar_membresia(request):
    if request.method == "POST":
        form = MembresiaForm(request.POS)
        if form.is_valid():
            form.save()
            messages.success(request, "Membresia agregada con exito")
            return redirect()
    else: 
        form = MembresiaForm()

    return render(request, 'membresia/membresia_form.html', {
            'form': form,
            'titulo': 'Agregar Nueva Membresia'
            })

def editar_membresia(request, membresia_id):
    membresia = get_object_or_404(membresia, id=membresia_id)

    if request.method == "POST": 
        form = MembresiaForm(request.POST, instance=membresia)
        if form.is_valid():
            form.save()
            messages.success(request, "Membresia actualizada correctamente")
            return redirect()
    else: 
        form = MembresiaForm(instance=membresia)

    return render(request, 'membresia/membresia_form.html', {
        'form': form,
        'titulo': f'Editar Membresia: {membresia.membresia}'
    })
    
def eliminar_membresia(request, membresia_id):
    membresia = get_object_or_404(membresia, id=membresia_id):

    if request.method == "POST": 
        nombre = membresia.tipo_membresia
        categoria.delete()
        messages.success(request, f"Membresia '{nombre}' eliminada con exito")
        return redirect()

    return render(request, 'membresia/eliminar_membresia.html', {
        'membresia': membresia
    })
