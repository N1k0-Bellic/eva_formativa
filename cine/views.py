from django.shortcuts import render, get_object_or_404, redirect
from .models import Pelicula, Genero, Ticket
from .forms import TicketForm

def inicio(request):
    peliculas = Pelicula.objects.select_related('genero').filter(en_cartelera=True)
    generos = Genero.objects.all()

    q = request.GET.get('q')
    if q:
        peliculas = peliculas.filter(titulo__icontains=q)

    genero_id = request.GET.get('genero')
    if genero_id:
        peliculas = peliculas.filter(genero_id=genero_id)

    context = {
        'peliculas': peliculas,
        'generos': generos,
        'busqueda': q or '',
        'genero_seleccionado': int(genero_id) if genero_id else '',
    }
    return render(request, 'cine/inicio.html', context)

def detalle_pelicula(request, id):
    pelicula = get_object_or_404(Pelicula.objects.select_related('genero'), id=id, en_cartelera=True)
    
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.pelicula = pelicula
            ticket.save()
            return redirect('cine:exito_ticket', ticket_id=ticket.id)
    else:
        form = TicketForm()

    context = {
        'pelicula': pelicula,
        'form': form,
    }
    return render(request, 'cine/detalle.html', context)

def exito_ticket(request, ticket_id):
    ticket = get_object_or_404(Ticket.objects.select_related('pelicula'), id=ticket_id)
    total_pagar = ticket.cantidad * ticket.pelicula.precio
    context = {
        'ticket': ticket,
        'total_pagar': total_pagar,
    }
    return render(request, 'cine/ticket_exitoso.html', context)