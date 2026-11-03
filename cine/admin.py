from django.contrib import admin
from django.utils.html import format_html
from .models import Genero, Pelicula, Ticket

@admin.register(Genero)
class GeneroAdmin(admin.ModelAdmin):
    list_display = ('nombre',)
    search_fields = ('nombre',)

@admin.register(Pelicula)
class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'genero', 'formatted_precio', 'en_cartelera', 'miniatura')
    list_filter = ('en_cartelera', 'genero')
    search_fields = ('titulo',)

    @admin.display(description='Precio')
    def formatted_precio(self, obj):
        return f"${obj.precio:,.0f}".replace(',', '.')

    @admin.display(description='Afiche')
    def miniatura(self, obj):
        if obj.afiche:
            return format_html('<img src="{}" style="height: 50px; border-radius: 4px;" />', obj.afiche.url)
        return "Sin afiche"

@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'pelicula', 'nombre_comprador', 'correo_comprador', 'cantidad', 'fecha_compra')
    list_filter = ('pelicula',)
    search_fields = ('codigo', 'nombre_comprador', 'correo_comprador')