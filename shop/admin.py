from django.contrib import admin
from shop.models import Pelicula, Juego, Libro, Musica

class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'director', 'fecha_estreno', 'stock', 'oferta')
    
class JuegoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'desarrollador', 'fecha_lanzamiento', 'stock', 'oferta')

class LibroAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'autor', 'fecha_publicacion', 'stock', 'oferta')  

class MusicaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'artista', 'fecha_lanzamiento', 'stock', 'oferta')

admin.site.register(Pelicula, PeliculaAdmin)
admin.site.register(Juego, JuegoAdmin)
admin.site.register(Libro, LibroAdmin)
admin.site.register(Musica, MusicaAdmin)
